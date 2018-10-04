class Common(object):

    def __init__(self,x):
        self.x = x
        self.y = x+3

    def sharedMethod(self):
        return self.x