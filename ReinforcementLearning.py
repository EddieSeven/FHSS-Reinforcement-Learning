

class ReinforcementLearning:
    def __init__(self):
        self.Q = {}
        self.time = 0
        self.channels = []

    def update_Q(self, state_action, reinforcement):
        self.Q[state_action] = reinforcement

    def update_state(self, new_channels):
        self.time += 1
        self.channels = new_channels

    def choose_next_hop(self):
        pass

    @staticmethod
    def state_action(time, channels, next_channel):
        return tuple(((time, channels), next_channel))

    def train(self, time):
        for round in time:
            next_hop = self.choose_next_hop()
            self.update_Q()
            self.update_state()
        pass

    def test(self):
        pass


a = {}
a[4] = 'b'
print(a)
a[4] = 'c'
print(a)