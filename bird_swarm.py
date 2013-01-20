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

def tekenlijn(canvas,ol,nl):
    canvas.create_line(ol.geefx(), ol.geefy(), nl.geefx(), nl.geefy(),fill='black', width=1, arrow=LAST)

def tekencirkel(canvas,nl,cirkel=None):
    __straal = g_groottevogel/2
    if cirkel is None:
        """CREATE"""
        cirkel = canvas.create_oval(nl.geefx()-__straal,nl.geefy()-__straal,nl.geefx()+__straal,nl.geefy()+__straal,fill='red',outline='black',width=1)
    else:
        """MOVE"""
        canvas.coords(cirkel,nl.geefx()-__straal,nl.geefy()-__straal,nl.geefx()+__straal,nl.geefy()+__straal)
    canvas.update()    
    return cirkel

class vogel:
    """Dit is een vogel"""

    def __init__(self, canvas):
        self.__canvas = canvas
        self.__ll = locatie()
        self.__repr = tekencirkel(self.__canvas,self.__ll)
        
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
            self.__ll.zetpunt(lijstvanpunten[0])
   #     self.__ll.zetpunt()
##        #boven of onder?
##        if self.__ll.geefx() >= midden.geefx():
##            self.__ll.zetx(self.__ll.geefx() - g_flapperafstand)
##        else:
##            self.__ll.zetx(self.__ll.geefx() + g_flapperafstand)
##        
##        if self.__ll.geefy() >= midden.geefy():
##            self.__ll.zety(self.__ll.geefy() - g_flapperafstand)
##        else:
##            self.__ll.zety(self.__ll.geefy() + g_flapperafstand)
            
    def flapper(self,midden):
        oudelocatie = locatie(self.geeflocatie().geefx(), self.geeflocatie().geefy())
        
        print('net voor zetten')
        self.zetlocatie(midden)
        print('net na zetten')
        print('juist voor tekenen')
        tekencirkel(self.__canvas,self.geeflocatie(),self.__repr)
        print('juist na tekenen')
        #tekenlijn(self.__canvas, oudelocatie, self.geeflocatie())
        self.__canvas.update()

class zwerm:
    """Deze zwerm bevat de vogels"""

    def __init__(self,aantalvogels,master):
        self.__lcanvas = Canvas(master,width=g_groottescherm,height=g_groottescherm)
        self.__lcanvas.pack()
        self.__vv = []
        count = 0
        while count < aantalvogels:
            self.__vv.append(self.addbird())
            count = count + 1
        print "%s vogels toegevoegd" % count

    def vlieg(self):
        random.shuffle(self.__vv)
        midden = self.geefmidden()
        for v in self.__vv:
            print('Dit is het midden: %s' % (midden))
            v.flapper(midden);

    def geefvogels(self):
        return self.__vv

    def geefaantalvogels(self):
        return len(self.__vv)

    def killbird(self):
        if self.geefaantalvogels() > 0:
            self.__vv.pop()

    def addbird(self):
        self.__v = vogel(self.__lcanvas)
        self.__lcanvas.create_oval(self.__v.geeflocatie().geefx()-3,self.__v.geeflocatie().geefy()-3,self.__v.geeflocatie().geefx()+3,self.__v.geeflocatie().geefy()+3,fill='red',outline='black',width=3)
        return self.__v


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
        return locatie(nieuwex, nieuwey)

    def vuldelucht(self):
        pass

class locatie:
    """De locatie van een vogel"""
    
    def __init__(self,x=None,y=None):
        if x is None and y is None:
            self.__p = Point(random.randint(0,g_groottescherm),random.randint(0,g_groottescherm))
        else:
            self.__p = Point(round(x,2),round(y,2))

    def __str__(self):
        return 'X%sY%s' % (self.__p.x, self.__p.y)

    def geefx(self):
        return self.__p.x

    def geefy(self):
        return self.__p.y

    def zetpunt(self, p):
        self.__p = Point(round(p.x,2),round(p.y,2))

    def geefpunt(self):
        return self.__p

    def zetx(self, x):
        self.__xloc = round(x,2)

    def zety(self, y):
        self.__yloc = round(x,2)

