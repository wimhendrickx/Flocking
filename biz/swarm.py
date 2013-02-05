class zwerm():
    '''De klasse vogel'''
    def __init__(self,aantal,ifv):
        open('log.txt', 'w').close() #We starten van een propere log
        self.__ifv = ifv
        self.__vv = []
        count = 0
        while count < aantal:
            self.addbird()
            count += 1
    
    def addbird(self):
        self.__vv.append(vogel(self,self.__ifv))
        
    def vlieg(self):
        random.shuffle(self.__vv)
        midden = self.geefmidden()
        for v in self.__vv:
            v.flapper(midden)
        self.logTick()

    def geefaantalvogels(self):
        return len(self.__vv)
    
    def geefmidden(self):
        xloccum,yloccum = 0,0
        for v in self.__vv:
            l = v.geeflocatie()
            xloccum = xloccum + l.geefx()
            yloccum = yloccum + l.geefy()
        nieuwex = float(xloccum / self.geefaantalvogels())
        nieuwey = float(yloccum / self.geefaantalvogels())
        return locatie(nieuwex, nieuwey)

    def geefvogels(self):
        return self.__vv

    def killbird(self):
        if self.geefaantalvogels() > 0:
            self.__vv.pop()

    def isLocationFree(self,doel):
        for v in self.__vv:
            l = v.geeflocatie()
##            print('%s %s %s %s %s %s' % (doel[0],doel[1], g_groottevogel/2, v.geeflocatie().geefx(),v.geeflocatie().geefy(),g_groottevogel/2))
            if intersect.isIntersectingCircles(doel[0],doel[1], g_groottevogel/2, v.geeflocatie().geefx(),v.geeflocatie().geefy(),g_groottevogel/2):
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