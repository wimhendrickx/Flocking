import Tkinter
import random
import time
##from sympy import *
##from sympy.geometry import *
import abc
import intersect
import datetime
import Queue
import threading
import random
import pdb

#GLOBALVARS
g_aantalvogels = 3
g_groottescherm = 600
g_groottevogel = 6
g_flapperafstand = 50
g_aantalticks = 10

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
            
class vogel():
    '''De klasse vogel'''
    def __init__(self,zwerm,ifv):
        self.__ifv = ifv
        self.__ll = locatie()
        self.__ifv.tekenvogel(self)
        self.__zwerm = zwerm
        
    def geeflocatie(self):
        return self.__ll

    def zetlocatie(self,midden):
        snijpunten = intersect.getIntersectingPoints(self.__ll.geefx(),self.__ll.geefy(), g_flapperafstand, midden.geefx(), midden.geefy())
        if len(snijpunten) == 2:
            #Er worden normaal altijd 2 punten gevonden. Nu moet er bepaald worden wel punt er het dichtst bij het midden ligt
            if intersect.distanceBetweenPoints(snijpunten[0][0],snijpunten[0][1],midden.geefx(),midden.geefy()) <= intersect.distanceBetweenPoints(snijpunten[1][0],snijpunten[1][1],midden.geefx(),midden.geefy()):
                doel = snijpunten[0]               
            else:
                doel = snijpunten[1]
            #Doel is nu het wiskundige punt dat zich het dichtst bij het midden bevindt
            #Nu moet er getest worden of we dit doel kunnen bereiken (botsingen)
            if self.__zwerm.isLocationFree(doel):
                self.__ll.zetpunt(doel[0],doel[1])
        else:
            pass

    def flapper(self,midden):
        oudelocatie = locatie(self.geeflocatie().geefx(), self.geeflocatie().geefy())
        self.zetlocatie(midden)
        self.__ifv.tekenvogel(self)

class GuiPart(object):
    def __init__(self, queue, endCommand): 
        self.queue = queue
        self.root = Tkinter.Tk()
        Tkinter.Canvas(self.root,width=g_groottescherm,height=g_groottescherm).pack()
        Tkinter.Button(self.root, text="Move 1 tick", command=self.doSomething).pack()
        self.vogelcords = {} #register of bird and their corresponding coordinates 
        
    def getRoot(self):
        return self.root
    
    def doSomething():
        pass #button action
    
    def processIncoming(self):
        """ Handle all messages currently in the queue, if any. """ 
        while self.queue.qsize( ):
            try:
                msg = self.queue.get(0)
                try:
                        vogel = msg
                        l = vogel.geeflocatie()
                        if self.vogelcords.has_key(vogel):
                            cirkel = self.vogelcords[vogel]
                            self.gcanvas.coords(cirkel,l.geefx()-g_groottevogel,l.geefy()-g_groottevogel,l.geefx()+g_groottevogel,l.geefy()+g_groottevogel)            
                        else:
                            cirkel = self.gcanvas.create_oval(l.geefx()-g_groottevogel,l.geefy()-g_groottevogel,l.geefx()+g_groottevogel,l.geefy()+g_groottevogel,fill='red',outline='black',width=1)
                            self.vogelcords[vogel] = cirkel 
                        self.gcanvas.update()
                except:
                    print('Failed, was van het type %' % type(msg))
            except Queue.Empty:
                pass

class ThreadedClient(object):

    def __init__(self):
        self.queue = Queue.Queue( )
        self.gui = GuiPart(self.queue, self.endApplication)
        self.root = self.gui.getRoot()
        self.running = True
        self.GuiThread = threading.Thread(target=self.workerGuiThread) 
        self.GuiThread.start()
            
    def workerGuiThread(self):
        while self.running:
            self.root.after(200, self.workerGuiThread)
            self.gui.processIncoming( )     

    def endApplication(self): 
        self.running = False
        
    def tc_TekenVogel(self,vogel):
        self.queue.put(vogel)

class formulier():
    '''Opstartklasse'''
    def start(self):
        self.gv = graphicvisualizer()
        self.z = zwerm(10,self.gv)
#         for t in range(1,g_aantalticks):
#             self.z.vlieg()
    
    def pressOneTickButton():
        self.z.vlieg()
    
    def __init__(self):
        pass

class ivisualizer(object):
    __metaclass__ = abc.ABCMeta
    '''Het contract waaraan de kinderen moeten voldoen'''
    
    @abc.abstractmethod
    def tekenvogel(self,vogel,nieuw):
        return
       
class graphicvisualizer(ivisualizer):
    '''Hier wordt de grafische interface gedefinieerd'''
    def __init__(self):
       self.client = ThreadedClient()
       
        
    def bindFunctions(self):
        pass
    
    def tekenvogel(self,vogel):
        self.client.tc_TekenVogel(vogel)
        # Dit wordt een taak van de ThreadedClient
        # Nog uitzoeken hoe een taak op de queue moet gezet worden
        

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

    def __str__(self):
        return '(%s:%s)' % (self.__xloc, self.__yloc)

    def geefx(self):
        return self.__xloc

    def geefy(self):
        return self.__yloc

    def geefpunt(self):
        return self.__p

    def zetx(self, x):
        self.__xloc = round(x,2)

    def zety(self, y):
        self.__yloc = round(y,2)

    def zetpunt(self, x, y):
        self.zetx(x)
	self.zety(y)
