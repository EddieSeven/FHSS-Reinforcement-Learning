from src.ReinforcementLearning import *
from src.Channel import Channel


def run_experiment(transmission_length, channel_length, epsilon, epsilon_decay_rate, iterations, learning_rate):
    channel = Channel()
    transmission_matrix = [[Channel() for y in range(channel_length)] for x in range(transmission_length)]
    channel.fillChannelTemplate(transmission_matrix)
    a = ReinforcementLearning()
    a.data = transmission_matrix
    a.train(epsilon, epsilon_decay_rate, iterations, learning_rate)

    channel.fillChannelTemplate(transmission_matrix)

    performance = a.test(transmission_matrix)

    print(performance * 100)
