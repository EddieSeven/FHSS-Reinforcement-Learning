import random
import copy

class Channel:
    def __init__(self, alpha=0.0, x=0.0, length=0, interference = 0.0,randDoub = 0):
        self.isEmpty = True
        self.alpha = alpha
        self.x = x
        self.length = length
        self.interference = interference
        self.name = 'ch'
        self.randDoub = randDoub

    def printData(self,transmissionMatrix,channelLength):
        for item in transmissionMatrix:
            print()
            for i in range(10):
                print('(',end='')
                print(item[i].x, end=',')
                print(item[i].alpha, end='')
                print(')', end ='')

    def __repr__(self):
        return self.name


def create_pattern(channel):
    channel.alpha = random.uniform(0, .20)
    channel.x = random.uniform(0, 0.5)
    channel.length = random.randint(1, 100)


def get_interference(channel):
    interference = random.uniform(0.5, 1)
    random_double = random.uniform(0, 1)
    if random_double < channel.alpha:
        interference -= channel.x

    return interference


def interference_noise(interference):
    plus_or_minus = random.random()
    if plus_or_minus < 0.5:
        return interference * 1.02
    else:
        return interference * 0.98


def create_matrix(channel_length, transmission_length):
    transmission_matrix = []
    for i in range(transmission_length):
        channels = []
        for j in range(channel_length):
            channel = Channel()
            channels.append(channel)
        transmission_matrix.append(channels)

    return transmission_matrix


def create_template(channel_length, transmission_length):
    template = create_matrix(channel_length, transmission_length)
    length = 0
    first_channel = None

    for channel in range(channel_length):
        for time in range(transmission_length):
            current_channel = template[time][channel]

            if length is 0:
                first_channel = current_channel
                create_pattern(first_channel)
                length = first_channel.length

            current_channel.alpha = first_channel.alpha
            current_channel.x = first_channel.x

            current_channel.name = "t" + str(time) + "c" + str(channel)
            length -= 1
        length = 0

    return template


def fill_template(channel_length, transmission_length, template):
    filled_template = copy.deepcopy(template)
    length = 0
    interference = 0
    first_channel = None

    for channel in range(channel_length):
        for time in range(transmission_length):
            if length is 0:
                first_channel = filled_template[time][channel]
                interference = get_interference(first_channel)
                first_channel.interference = interference
                length = first_channel.length
            else:
                filled_template[time][channel].interference = interference_noise(interference)

            length -= 1
        length = 0

    return filled_template

def format_double(d):
    return "{0:.2f}".format(d)


# Chan = Channel()
# tranLength = 10000
# channelLength = 10
# transmissionMatrix = [[Channel() for y in range(channelLength)] for x in range(tranLength)]
# Chan.fillChannelTemplate(transmissionMatrix,channelLength,tranLength)
# Chan.printData(transmissionMatrix)
