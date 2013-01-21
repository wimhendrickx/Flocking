"""Mijn eerste module"""
import random
import time
from Tkinter import *
from sympy import *
from sympy.geometry import *

#GLOBALVARS
g_aantalvogels = 3
g_groottescherm = 600
g_groottevogel = 6
g_flapperafstand = 50
g_aantalticks = 10

##def tekenlijn(canvas,ol,nl):
##    """Deze dient enkel om de vogels een visueel spoor achter te laten"""
##    canvas.create_line(ol.geefx(), ol.geefy(), nl.geefx(), nl.geefy(),fill='black', width=1, arrow=LAST)
##
##def tekencirkel(canvas,nl,cirkel=None):
##    __straal = g_groottevogel/2
##    if cirkel is None:
##        """CREATE"""
##        cirkel = canvas.create_oval(nl.geefx()-__straal,nl.geefy()-__straal,nl.geefx()+__straal,nl.geefy()+__straal,fill='red',outline='black',width=1)
##    else:
##        """MOVE"""
##        canvas.coords(cirkel,nl.geefx()-__straal,nl.geefy()-__straal,nl.geefx()+__straal,nl.geefy()+__straal)
##    canvas.update()    
##    return cirkel

class gvogel(object):
    """Dit is de grafische superklasse van zwerm, om zo de specieke grafische opdrachten uit de klasse te weren"""
    def __init__(self, l):
        # Hier zou de gvogel ook toegang moeten krijgen tot het canvas ...
        pass

    def tekenmezelf(self, nieuw):
        if nieuw:
            cirkel = gcanvas.create_oval(l.geefx()-__straal,l.geefy()-__straal,l.geefx()+__straal,l.geefy()+__straal,fill='red',outline='black',width=1)
        else:
            gcanvas.coords(cirkel,l.geefx()-__straal,l.geefy()-__straal,l.geefx()+__straal,l.geefy()+__straal)
        canvas.update()
#        gcanvas.create_oval(self.__v.geeflocatie().geefx()-3,self.__v.geeflocatie().geefy()-3,self.__v.geeflocatie().geefx()+3,self.__v.geeflocatie().geefy()+3,fill='red',outline='black',width=3)

class vogel(gvogel):
    """Dit is een vogel"""

    def __init__(self):
        self.__ll = locatie()
        super(vogel,self).__init__(self.__ll)
        super(vogel,self).tekenmezelf(True)
        
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
        print('net na zetten')
        print('juist voor tekenen')
        #tekencirkel(self.__canvas,self.geeflocatie(),self.__repr)
        super.tekenmezelf(False) #Dit is nu een taak van de superklasse
        print('juist na tekenen')
        #tekenlijn(self.__canvas, oudelocatie, self.geeflocatie())
        self.__canvas.update()

class gzwerm(object):
    """Dit is de grafische superklasse van zwerm, om zo de specieke grafische opdrachten uit de klasse te weren"""
  
    def __init__(self):
        master = Tk()
        gcanvas = Canvas(master,width=g_groottescherm,height=g_groottescherm)
        gcanvas.pack()             

class zwerm(gzwerm):
    """Deze zwerm bevat de vogels"""

    def __init__(self,aantalvogels,master):
        super(zwerm, self).__init__()
        self.__vv = []
        count = 0
        while count < aantalvogels:
            self.addbird()
            count = count + 1
##        print "%s vogels toegevoegd" % count

    def vlieg(self):
        random.shuffle(self.__vv)
        midden = self.geefmidden()
        for v in self.__vv:
            print('Dit is het midden: %s, %s' % (float(midden.geefx()), float(midden.geefy())))
            v.flapper(midden);

    def geefvogels(self):
        return self.__vv

    def geefaantalvogels(self):
        return len(self.__vv)

    def killbird(self):
        if self.geefaantalvogels() > 0:
            self.__vv.pop()

    def addbird(self):
        self.__v = vogel()
        self.__vv.append(self.__v)

##    def bepaalmidden(self):
##        count,xloccum,yloccum = 0,0,0
##        while count < self.geefaantalvogels():
##            l = self.__vv[count].geeflocatie()
##            xloccum = xloccum + l.geefx()
##            yloccum = yloccum + l.geefy()
##            count = count + 1
##        xloccum = xloccum/self.geefaantalvogels()
##        yloccum = yloccum/self.geefaantalvogels()
##        self.__lcanvas.create_oval(xloccum-6,yloccum-6,xloccum+6,yloccum+6,fill='blue',outline='black',width=3)
##        middenloc = locatie()
##        middenloc.zetx(xloccum)
##        middenloc.zety(yloccum)
 
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
        return locatie(x=nieuwex, y=nieuwey)

    def vuldelucht(self):
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
