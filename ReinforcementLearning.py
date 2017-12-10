import random


class ReinforcementLearning:
    def __init__(self):
        self.Q = {}
        self.data = [[]]

    def update_Q(self, time, action, next_time, next_action, interference):
        self.Q[(time, action)] = interference + self.Q[(next_time, next_action)]

    def get_channels(self, time):
        return self.data[time]

    def action(self, epsilon, time):
        alpha = random.random()
        channels = self.get_channels(time)

        if alpha < epsilon:
            return random.choice(channels)
        else:
            return self.get_Qmin(time)

    def train(self, epsilon, epsilon_decay_factor, duration):

        for time in range(duration):
            epsilon *= epsilon_decay_factor
            action = self.action(epsilon, time)
            next_time = time + 1

            if next_time < duration:
                next_action = self.action(epsilon, next_time)
                self.update_Q(time, action, next_time, next_action)

        pass

    def test(self):
        pass

    def get_Qmin(self, time):  # todo handle end of q table border case
        next_channels = self.get_channels(time + 1)
        lowest_reinforcement = 1
        optimal_channel = next_channels[0]

        for next_channel in next_channels:
            reinforcement = self.Q.get((time, next_channel))
            if reinforcement < lowest_reinforcement:
                optimal_channel = next_channel
                lowest_reinforcement = reinforcement

        return optimal_channel


def to_tuple(time, channel, next_channel):
    return tuple(((time, channel), next_channel))


q = {}
data = [[]]

for i in range (10000):
    for j in range(10):
        channel = 'c' + str(j + 1)
        interference = random.random()



q = {(0, 'c1'): 0.56, (0, 'c2'): 0.3}
data = [['c1', 'c2'], ['c1', 'c2'], ['c1', 'c2']]
a = ReinforcementLearning()
a.Q = q
a.data = data
print(a.get_Qmin(0))
