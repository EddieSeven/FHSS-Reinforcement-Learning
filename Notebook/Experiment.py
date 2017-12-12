from src.ReinforcementLearning import *
from src.Channel import *


def mean(collection):
    sum_of_elements = 0
    for element in collection:
        sum_of_elements += element

    return sum_of_elements / len(collection)


def run_experiment(transmission_length, channel_length, epsilon, epsilon_decay_rate, training_iterations, learning_rate, train_runs, test_runs):
    algorithim = ReinforcementLearning()
    performances = []
    template = create_template(channel_length, transmission_length)

    for _ in range(train_runs):
        training_matrix = fill_template(channel_length, transmission_length, template)
        algorithim.data = training_matrix
        algorithim.train(epsilon, epsilon_decay_rate, training_iterations, learning_rate)

    print("Done Training")

    for _ in range(test_runs):
        test_matrix = fill_template(channel_length, transmission_length, template)
        algorithim.data = test_matrix
        performance = algorithim.test(test_matrix)
        performances.append(performance)

    return mean(performances)


