from src.ReinforcementLearning import *
from src.Channel import Channel


def mean(collection):
    sum_of_elements = 0
    for element in collection:
        sum_of_elements += element

    return sum_of_elements / len(collection)


def run_experiment(transmission_length, channel_length, epsilon, epsilon_decay_rate, training_iterations, learning_rate, train_runs, test_runs):
    channel = Channel()
    channel.createChannelData()
    algorithim = ReinforcementLearning()
    performances = []

    for _ in range(train_runs):
        training_matrix = channel.fillChannelTemplate(channel_length, transmission_length)
        algorithim.data = training_matrix
        algorithim.train(epsilon, epsilon_decay_rate, training_iterations, learning_rate)

    print("Done Training")

    for _ in range(test_runs):
        test_matrix = channel.fillChannelTemplate(channel_length, transmission_length)
        algorithim.data = test_matrix
        performance = algorithim.test(test_matrix)
        performances.append(performance)

    return mean(performances)


transmission_length = 1000
channel_length = 10
epsilon = 0.999
epsilon_decay_rate = 0.999
training_iterations = 100
learning_rate = 0.99
train_runs = 5
test_runs = 100

performance = run_experiment(transmission_length, channel_length, epsilon, epsilon_decay_rate, training_iterations, learning_rate, train_runs, test_runs)
print(performance)



