class location:
    """The location of a bird"""
    
    def __init__(self,x=None,y=None):
        if x is None and y is None:
            self.__xloc = random.randint(0, g_groottescherm)
            self.__yloc = random.randint(0, g_groottescherm)
            else:
            self.__xloc = round(float(x), 2)
            self.__yloc = round(float(y), 2)

    def __str__(self):
        return '(%s:%s)' % (self.__xloc, self.__yloc)

    def getX(self):
        return self.__xloc

    def getY(self):
        return self.__yloc

    def getPoint(self):
        return self.__p

    def setX(self, x):
        self.__xloc = round(x,2)

    def setY(self, y):
        self.__yloc = round(y,2)

    def setPoint(self, x, y):
        self.setX(x)
	    self.setY(y)