import random

class Channel:
    def __init__(self, alpha=0.0, x=0.0, length=0, interference = 0.0,randDoub = 0):
        self.isEmpty = True
        self.alpha = alpha
        self.x = x
        self.length = length
        self.interference = interference
        self.name = 'ch'
        self.randDoub = randDoub


    def createChannelData(self):
        alpha = random.uniform(0, .2)
        x = random.uniform(.5, 1)
        length = random.randint(1, 100)
        interference = random.uniform(.5,1)
        randDoub = random.uniform(0,1)

        return alpha, x, length, interference, randDoub

    def fillChannelTemplate(self,transmissionMatrix):

        length = 0

        for channel in range(10):
            for time in range(10000):
                if length is 0:
                    alpha, x, length, interference, randDoub = self.createChannelData()

                if randDoub < alpha:
                    interference -= x

                transmissionMatrix[time][channel].alpha = alpha
                transmissionMatrix[time][channel].interference = interference
                transmissionMatrix[time][channel].x = x
                transmissionMatrix[time][channel].isEmpty = False
                length -= 1

    def __repr__(self):
        return self.name

    def printData(self,transmissionMatrix):
        for item in transmissionMatrix:
            print()
            for i in range(10):
                print('(',end='')
                print(item[i].x, end=',')
                print(item[i].alpha, end='')
                print(')', end ='')
                
                
                
    
    def __repr__(self):
        return self.name


# Chan = Channel()
# transmissionMatrix = [[Channel() for y in range(10)] for x in range(10000)]
# Chan.fillChannelTemplate(transmissionMatrix)
# Chan.printData(transmissionMatrix)
