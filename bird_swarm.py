from Tkinter import *
import random
import time
from sympy import *
from sympy.geometry import *
import abc

#GLOBALVARS
g_aantalvogels = 3
g_groottescherm = 600
g_groottevogel = 6
g_flapperafstand = 50
g_aantalticks = 10

class formulier():
    '''Opstartklasse'''
    def start(self,ifv):
        z = zwerm(10,ifv)
        for t in range(1,g_aantalticks):
            z.vlieg()
    def drukopdemoknop(self):
        self.start(graphicvisualizer())

    def __init__(self):
        pass

class zwerm():
    '''De klasse vogel'''
    def __init__(self,aantal,ifv):
        self.__ifv = ifv
        self.__vv = []
        count = 0
        while count < aantal:
            self.addbird()
            count += 1
    
    def addbird(self):
        self.__vv.append(vogel(self.__ifv))
        
    def vlieg(self):
        random.shuffle(self.__vv)
        midden = self.geefmidden()
        for v in self.__vv:
##            print('Dit is het midden: %s, %s' % (float(midden.geefx()), float(midden.geefy())))
            v.flapper(midden);

    def geefaantalvogels(self):
        return len(self.__vv)
    
    def geefmidden(self):
        xloccum,yloccum = 0,0
        print "%s vogels te testen" % len(self.__vv)
        for v in self.__vv:
            l = v.geeflocatie()
            print('dit is de inputlocatie voor geefmidden: %s' % (l))
            xloccum = xloccum + l.geefx()
            yloccum = yloccum + l.geefy()
        nieuwex = float(xloccum / self.geefaantalvogels())
        nieuwey = float(yloccum / self.geefaantalvogels())
        print "nieuwe x: %s; nieuwe y: %s" % (nieuwex, nieuwey)
        return locatie(nieuwex, nieuwey)

    def geefvogels(self):
        return self.__vv

    def killbird(self):
        if self.geefaantalvogels() > 0:
            self.__vv.pop()
            
class vogel():
    '''De klasse vogel'''
    def __init__(self,ifv):
        self.__ifv = ifv
        self.__ll = locatie()
        self.__ifv.tekenvogel(self)
        
    def geeflocatie(self):
        return self.__ll

    def zetlocatie(self,midden):
        print('punt: %s en midden: %s' % (self.geeflocatie(),midden))
        lijnstukvogelmidden = Segment(self.geeflocatie().geefpunt(),midden.geefpunt())
        cirkelvelocityvogel = Circle(self.geeflocatie().geefpunt(),g_flapperafstand)
        lijstvanpunten = intersection(lijnstukvogelmidden,cirkelvelocityvogel)
        if len(lijstvanpunten) == 0:
            print('geen punten gevonden')
        else:
            print('punten gevonden')
	    print "punt: {0}, x: {1}, y: {2}".format(lijstvanpunten[0], lijstvanpunten[0].x, lijstvanpunten[0].y)
            self.__ll.zetpunt(x=float(lijstvanpunten[0].x), y=float(lijstvanpunten[0].y))

    def flapper(self,midden):
        oudelocatie = locatie(self.geeflocatie().geefx(), self.geeflocatie().geefy())
        print('net voor zetten')
        self.zetlocatie(midden)
        self.__ifv.tekenvogel(self)
        print('net na zetten')
        print('juist voor tekenen')
        #tekencirkel(self.__canvas,self.geeflocatie(),self.__repr)
        ##super.tekenmezelf(False) #Dit is nu een taak van de superklasse
        print('juist na tekenen')
        #tekenlijn(self.__canvas, oudelocatie, self.geeflocatie())

class ivisualizer(object):
    __metaclass__ = abc.ABCMeta
    '''Het contract waaraan de kinderen moeten voldoen'''
    
    @abc.abstractmethod
    def tekenvogel(self,vogel,nieuw):
        return
       
class graphicvisualizer(ivisualizer):
    '''Hier wordt de grafische interface gedefinieerd'''
    def __init__(self):
        master = Tk()
        self.gcanvas = Canvas(master,width=g_groottescherm,height=g_groottescherm)
        self.gcanvas.pack()
        self.vogelcords = {}
        
    def tekenvogel(self,vogel):
        l = vogel.geeflocatie()
        if self.vogelcords.has_key(vogel):
            cirkel = self.vogelcords[vogel]
            self.gcanvas.coords(cirkel,l.geefx()-g_groottevogel,l.geefy()-g_groottevogel,l.geefx()+g_groottevogel,l.geefy()+g_groottevogel)            
        else:
            cirkel = self.gcanvas.create_oval(l.geefx()-g_groottevogel,l.geefy()-g_groottevogel,l.geefx()+g_groottevogel,l.geefy()+g_groottevogel,fill='red',outline='black',width=1)
            self.vogelcords[vogel] = cirkel 
        self.gcanvas.update()

class testvisualizer(ivisualizer):
    def __init__(self):
        pass

    def tekenvogel(self,vogel):
        pass

class locatie:
    """De locatie van een vogel"""
    
    def __init__(self,x=None,y=None):
        if x is None and y is None:
	    self.__xloc = random.randint(0, g_groottescherm)
	    self.__yloc = random.randint(0, g_groottescherm)
        else:
	    self.__xloc = round(float(x), 2)
	    self.__yloc = round(float(y), 2)
	self.resetpunt()

    def __str__(self):
        return 'X%sY%s' % (self.__p.x, self.__p.y)

    def geefx(self):
        return self.__xloc

    def geefy(self):
        return self.__yloc

    def resetpunt(self):
        self.__p = Point(self.__xloc, self.__yloc)

    def geefpunt(self):
        return self.__p

    def zetx(self, x):
        self.__xloc = round(x,2)
	self.resetpunt()

    def zety(self, y):
        self.__yloc = round(y,2)
	self.resetpunt()

    def zetpunt(self, x, y):
        self.zetx(x)
	self.zety(y)
