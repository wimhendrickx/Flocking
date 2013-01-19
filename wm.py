"""Mijn eerste module"""
import random
import time
from tkinter import *
from sympy import *
from sympy.geometry import *

v = Point(0,0)
m = Point(10,25)
lijnvm = Segment(v,m)
cirkel = Circle(v,1)
print (intersection(lijnvm,cirkel))
>>> [Point(2*sqrt(29)/29, 5*sqrt(29)/29)]



#GLOBALVARS
g_aantalvogels = 20
g_groottescherm = 1000
g_groottevogel = 6
g_flapperafstand = 50
g_aantalticks = 10

def tekenlijn(canvas,ol,nl):
    print ('tekenlijn: oude {0} en nieuwe {1}'.format(ol,nl))
    canvas.create_line(ol.geefx(), ol.geefy(), nl.geefx(), nl.geefy(),
fill='black', width=3, arrow=LAST)
    print ('teken')

class vogel:
    """Dit is een vogel"""

    def __init__(self, canvas):
        self.__canvas = canvas
        self.__ll = locatie()
        self.__repr = self.__canvas.create_oval(self.geeflocatie().geefx()-3,self.geeflocatie().geefy()-3,self.geeflocatie().geefx()+3,self.geeflocatie().geefy()+3,fill='red',outline='black',width=3)

    def geeflocatie(self):
        return self.__ll

    def zetlocatie(self,midden):
        print ('oudex {0}'.format(self.__ll.geefx()))
        self.__ll.zetx(self.__ll.geefx() + g_flapperafstand)
        print ('nieuwex {0}'.format(self.__ll.geefx()))
        self.__ll.zety(self.__ll.geefy() + g_flapperafstand)
        if(

    def flapper(self,midden):
        oudelocatie = locatie()
        oudelocatie = self.geeflocatie()
        print ('flapperoude: {0}'.format(oudelocatie))
        self.zetlocatie(midden)
        self.__canvas.coords(self.__repr,self.geeflocatie().geefx()-3,self.geeflocatie().geefy()-3,self.geeflocatie().geefx()+3,self.geeflocatie().geefy()+3)
        nieuwelocatie = self.geeflocatie()
        print ('flappernieuwe: {0} flapperoude:{1}'.format(nieuwelocatie,oudelocatie))
        tekenlijn(self.__canvas, oudelocatie, nieuwelocatie)
        self.__canvas.update()

class zwerm:
    """Deze zwerm bevat de vogels"""

    def __init__(self,aantalvogels,master):
        self.__lcanvas = Canvas(master, width=g_groottescherm,height=g_groottescherm)
        self.__lcanvas.pack()
        self.__vv = []
        #aantalvogels = 5
        count = 0
        while count < aantalvogels:
            self.__vv.append(self.addbird())
            count = count + 1
        print(self.geefaantalvogels())

    def vlieg(self):
        random.shuffle(self.__vv)
        print ('vlieg')
        for v in self.__vv:
            v.flapper(self.bepaaldmidden());

    def geefaantalvogels(self):
        return len(self.__vv)

    def killbird(self):
        if self.geefaantalvogels() > 0:
            self.__vv.pop()
        else:
            print ('Geen vogelse meer te killen')
        print (self.geefaantalvogels())

    def addbird(self):
        #eigenlijk zou de vogel zichzelf moeten gaan tekenen
        self.__v = vogel(self.__lcanvas)
        #print (self.__v.geeflocatie().geefx())
        self.__lcanvas.create_oval(self.__v.geeflocatie().geefx()-3,self.__v.geeflocatie().geefy()-3,self.__v.geeflocatie().geefx()+3,self.__v.geeflocatie().geefy()+3,fill='red',outline='black',width=3)
        return self.__v
        #print (self.geefaantalvogels())

    def bepaalmidden(self):
        count,xloccum,yloccum = 0,0,0
        while count < self.geefaantalvogels():
            print (self.__vv[count].geeflocatie())
            l = self.__vv[count].geeflocatie()
            xloccum = xloccum + l.geefx()
            yloccum = yloccum + l.geefy()
            count = count + 1
        xloccum = xloccum/self.geefaantalvogels()
        yloccum = yloccum/self.geefaantalvogels()
        #print ('het midden is %s,%s' % (xloccum/self.geefaantalvogels(), yloccum/self.geefaantalvogels()))
        self.__lcanvas.create_oval(xloccum-6,yloccum-6,xloccum+6,yloccum+6,fill='blue',outline='black',width=3)
        middenloc = locatie()
        middenloc.zetx(xloccum)
        middenloc.zety(yloccum)
    
    def vuldelucht(self):
        pass
        #self.__lcanvas.create_oval(50,50,100,100,fill='red',outline='black',width=3)
        #master.pack()


class locatie:
    """De locatie van een vogel"""

    def __init__(self):
        self.__xloc = random.randint(0,g_groottescherm)
        self.__yloc = random.randint(0,g_groottescherm)

    def __str__(self):
        return 'de locatie is %s,%s' % (self.__xloc, self.__yloc)

    def geefx(self):
        return self.__xloc

    def geefy(self):
        return self.__yloc

    def zetx(self, x):
        self.__xloc = x

    def zety(self, y):
        self.__yloc = y

#z.bepaalmidden()
master = Tk()
z = zwerm(g_aantalvogels,master)
#z.vuldelucht()
z.bepaalmidden()
#master.pack()
for t in range(1,g_aantalticks):
    z.vlieg()
    time.sleep(0.05)
master.mainloop()





    def __init__(self, par1, par2=None):
# do something with par1

if par2 is None:
print "par2 was not given!"
else:
print "par2 is", par2
