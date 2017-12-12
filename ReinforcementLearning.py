import random
from Channel import Channel


class ReinforcementLearning:
    def __init__(self):
        self.Q = {}
        self.data = [[]]

    def update_reinforcement(self, time, move, learning_rate):
        if move is not self.get_q_move(time):
            self.Q[(time, move)] *= learning_rate
        else:
            self.Q[(time, move)] *= (1 - learning_rate) + 1

    def get_channels(self, time):
        return self.data[time]

    def get_move(self, epsilon, time):
        alpha = random.random()
        next_channels = self.get_channels(time + 1)

        if alpha < epsilon:
            next_hop = random.choice(next_channels)
            return next_channels.index(next_hop)
        else:
            return self.get_q_move(time)

    def train(self, epsilon, epsilon_decay_factor, iterations, learning_rate):
        duration = len(self.data)
        for _ in range(iterations):
            epsilon *= epsilon_decay_factor

            for time in range(duration):
                next_time = time + 1

                if next_time < duration:
                    self.initialize_q(time)
                    move = self.get_move(epsilon, time)
                    self.update_reinforcement(time, move, learning_rate)

    def test(self, data):
        duration = len(self.data)
        number_incorrect = 0

        for time in range(duration):
            next_time = time + 1
            if next_time < duration:
                move = self.get_q_move(time)
                if is_optimal(move, data[time + 1]):
                    number_incorrect += 1

        return 1 - (number_incorrect / duration)

    def initialize_q(self, time):
        next_channels = self.get_channels(time + 1)

        for next_channel in next_channels:
            index = next_channels.index(next_channel)
            if self.Q.get((time, index), -1) == -1:
                self.Q[(time, index)] = 100.0

    def get_q_move(self, time):
        next_channels = self.get_channels(time + 1)
        highest_reinforcement = 0
        optimal_channel = 0

        for next_channel in next_channels:
            index = next_channels.index(next_channel)
            reinforcement = self.Q.get((time, index))
            if reinforcement > highest_reinforcement:
                optimal_channel = index
                highest_reinforcement = reinforcement

        return optimal_channel


def is_optimal(move, channels):
    optimal_channel = channels[0]

    for channel in channels:
        if channel.interference < optimal_channel.interference:
            optimal_channel = channel

    if move == channels.index(optimal_channel):
        return True
    else:
        return False


Chan = Channel()
time = 10000
transmissionMatrix = [[Channel() for y in range(10)] for x in range(time)]
Chan.fillChannelTemplate(transmissionMatrix)
a = ReinforcementLearning()
a.data = transmissionMatrix
a.train(0.999, 0.999, 10000, 0.99)

Chan.fillChannelTemplate(transmissionMatrix)

performance = a.test(transmissionMatrix)

print(performance * 100)