import random
from src.Channel import Channel


class ReinforcementLearning:
    def __init__(self):
        self.Q = {}
        self.data = [[]]

    def update_reinforcement(self, time, move, learning_rate, next_channels):
        if move == get_optimal_move(next_channels):
            self.Q[(time, move)] *= (1 - learning_rate) + 1
        else:
            self.Q[(time, move)] *= learning_rate

    def get_channels(self, time):
        return self.data[time]

    def get_next_channels(self, time):
        return self.data[time + 1]

    def get_move(self, epsilon, time, next_channels):
        alpha = random.random()

        if alpha < epsilon:
            next_hop = random.choice(next_channels)
            return next_channels.index(next_hop)
        else:
            return self.get_q_move(time, next_channels)

    def train(self, epsilon, epsilon_decay_factor, iterations, learning_rate):
        duration = len(self.data)
        for _ in range(iterations):
            epsilon *= epsilon_decay_factor

            for time in range(duration):
                next_time = time + 1

                if next_time < duration:
                    next_channels = self.get_next_channels(time)
                    self.initialize_q(time, next_channels)
                    move = self.get_move(epsilon, time, next_channels)
                    self.update_reinforcement(time, move, learning_rate, next_channels)

    def test(self, data):
        duration = len(self.data)
        number_incorrect = 0

        for time in range(duration):
            next_time = time + 1

            if next_time < duration:
                move = self.get_q_move(time, self.get_next_channels(time))
                if is_not_optimal(move, data[time + 1]):
                    number_incorrect += 1

        return 1 - (number_incorrect / duration)

    def initialize_q(self, time, next_channels):
        for channel in next_channels:
            index = next_channels.index(channel)
            if self.Q.get((time, index), -1) == -1:
                self.Q[(time, index)] = 100.0

    def get_q_move(self, time, next_channels):
        highest_reinforcement = 0
        optimal_channel = 0

        for channel in next_channels:
            index = next_channels.index(channel)
            reinforcement = self.Q.get((time, index))

            if reinforcement > highest_reinforcement:
                optimal_channel = index
                highest_reinforcement = reinforcement

        return optimal_channel


def get_optimal_move(next_channels):
    optimal_channel = next_channels[0]

    for channel in next_channels:
        if channel.interference < optimal_channel.interference:
            optimal_channel = channel

    return next_channels.index(optimal_channel)


def is_not_optimal(move, next_channels):
    optimal_move = get_optimal_move(next_channels)

    if move == optimal_move:
        return False
    else:
        return True
