import random
from Channel import Channel


class ReinforcementLearning:
    def __init__(self):
        self.Q = {}
        self.data = [[]]

    def check_optimal(self, time, move, learning_rate):
        if move is not self.get_Qmax(time):
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
            return self.get_Qmax(time)

    def train(self, epsilon, epsilon_decay_factor, duration, iterations, learning_rate):
        for _ in range(iterations):
            epsilon *= epsilon_decay_factor

            for time in range(duration):
                next_time = time + 1

                if next_time < duration:
                    self.initialize_Q_time(time)
                    move = self.get_move(epsilon, time)
                    self.check_optimal(time, move, learning_rate)


    def test(self):
        pass

    def initialize_Q_time(self, time):
        next_channels = self.get_channels(time + 1)

        for next_channel in next_channels:
            index = next_channels.index(next_channel)
            if self.Q.get((time, index), -1) == -1:
                self.Q[(time, index)] = 100.0

    def get_Qmax(self, time):  # todo handle end of q table border case
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

data = []

for i in range(10000):
    round = []
    for j in range(10):
        channel = Channel()
        channel.interference = random.random()
        channel.name = 'c' + str(j) + 't' + str(i)
        round.append(channel)
    data.append(round)


a = ReinforcementLearning()
a.data = data
a.train(0.999, 0.999, 10000, 100, 0.95)
print(a.Q)