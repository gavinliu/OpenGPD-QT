class TouchEvent:
    def __init__(self, x, y, action):
        self.x = x
        self.y = y
        self.action = action

    def __repr__(self):
        return 'TouchEvent X : %s , Y : %d' % (self.x, self.y)
