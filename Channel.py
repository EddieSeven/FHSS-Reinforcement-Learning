class Channel:
    def __init__(self, alpha=0.0, x=0.0, length=0):
        self.isEmpty = True
        self.alpha = alpha
        self.x = x
        self.length = length
        self.interference = 0
        self.name = 'ch'

    def __repr__(self):
        return self.name
