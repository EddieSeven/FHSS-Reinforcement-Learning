import random


class ReinforcementLearning:
    def __init__(self):
        self.Q = {}
        self.data = [[]]

    def update_Q(self, state_action, reinforcement):
        self.Q[state_action] = reinforcement

    def get_channels(self, time):
        return self.data[time]

    def next_hop(self, epsilon, channels):
        chooser = random.random()
        if chooser < epsilon:
            return random.choice(channels)
        else:
            return None

    @staticmethod
    def state_action(time, channels, next_channel):
        return tuple(((time, channels), next_channel))

    def train(self, time):
        for round in time:
            next_hop = self.next_hop()
            self.update_Q()
            self.update_state()
        pass

    def test(self):
        pass


a = [['c1', 'c2', 'c3'], ['c1', 'c2', 'c3']]
b = a[1]
print(b)