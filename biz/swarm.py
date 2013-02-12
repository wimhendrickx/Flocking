class swarm():
    def __init__(self,aantal,ifv):
        open('log.txt', 'w').close() #We starten van een propere log
        self.__ifv = ifv
        self.__vv = []
        count = 0
        while count < aantal:
            self.addBird()
            count += 1
    
    def addBird(self):
        self.__vv.append(bird(self,self.__ifv))
        
    def move(self):
        random.shuffle(self.__vv)
        centre = self.getCentre()
        for v in self.__vv:
            v.fly(centre)
        self.logTick()

    def getNumberOfBirds(self):
        return len(self.__vv)
    
    def getCentre(self):
        xloccum,yloccum = 0,0
        for v in self.__vv:
            l = v.getLocation()
            xloccum = xloccum + l.getX()
            yloccum = yloccum + l.getY()
        nieuwex = float(xloccum / self.getNumberOfBirds())
        nieuwey = float(yloccum / self.getNumberOfBirds())
        return location(nieuwex, nieuwey)

    def getBirds(self):
        return self.__vv

    def killBird(self):
        if self.getNumberOfBirds() > 0:
            self.__vv.pop()

    def isLocationFree(self,target):
        for v in self.__vv:
            l = v.geeflocatie()
##            print('%s %s %s %s %s %s' % (doel[0],doel[1], g_groottevogel/2, v.geeflocatie().geefx(),v.geeflocatie().geefy(),g_groottevogel/2))
            if intersect.isIntersectingCircles(target[0],target[1], g_groottevogel/2, v.geeflocatie().geefx(),v.geeflocatie().geefy(),g_groottevogel/2):
                #Er bevindt zich een vogel op dit doel!
                return False
        return True
    
    def logTick(self):
        with open('log.txt','a') as f:
            now = datetime.datetime.now()
            f.write('TICK @ %s\n' % now.strftime("%Y-%m-%d %H:%M:%S"))
            for v in self.__vv:
                f.write('\t%s\n' % str(v.geeflocatie()))
        f.closed