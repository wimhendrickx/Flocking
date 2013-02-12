import mtTkinter as Tkinter
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

class GuiPart(object):
    def __init__(self, queue, endCommand): 
#         pdb.set_trace()
        self.queue = queue
    
    def doSomething():
        pass #button action
    
    def setRoot(self, root):
        self.root = root
    
    def drawGeneral(self):
        print ('draw general')
        self.gcanvas = Tkinter.Canvas(self.root,width=g_groottescherm,height=g_groottescherm)
        self.gcanvas.pack()
        self.gbutton = Tkinter.Button(self.root, text="Move 1 tick", command=self.doSomething).pack()
        self.vogelcords = {} #register of bird and their corresponding coordinates  
    
    def processIncoming(self):
        if self.queue.qsize() > 0:
            print ('processIncoming %s' % self.queue.qsize())
        try:
            msg = self.queue.get(0)
            #try:
            vogel = msg
            l = vogel.geeflocatie()
            if self.vogelcords.has_key(vogel):
                cirkel = self.vogelcords[vogel]
                self.gcanvas.coords(cirkel,l.geefx()-g_groottevogel,l.geefy()-g_groottevogel,l.geefx()+g_groottevogel,l.geefy()+g_groottevogel)            
            else:
                cirkel = self.gcanvas.create_oval(l.geefx()-g_groottevogel,l.geefy()-g_groottevogel,l.geefx()+g_groottevogel,l.geefy()+g_groottevogel,fill='red',outline='black',width=1)
                self.vogelcords[vogel] = cirkel 
            self.gcanvas.update()
            #except:
            #    print('damn niet gelukt')
        except Queue.Empty:
            pass

class ThreadedClient(object): 
    
    def __init__(self):
        self.queue = Queue.Queue( )
        self.gui = GuiPart(self.queue, self.endApplication)
        self.root = 0
        self.running = True
        self.GuiThread = threading.Thread(target=self.workerGuiThread) 
        self.GuiThread.start()
        print ('kom ik wel na de guithread.start?')
            
    def workerGuiThread(self):
        if self.root == 0:
            self.root = Tkinter.Tk()
            self.gui.setRoot(self.root)
            self.gui.drawGeneral()
            self.root.mainloop()
        while self.running:
            self.root.after(200, self.workerGuiThread)
            self.gui.processIncoming()     

    def endApplication(self): 
        self.running = False
        
    def tc_TekenVogel(self,vogel):
        print('vul ik de queue wel?')
        self.queue.put(vogel)

class formulier():
    '''Opstartklasse'''
    def start(self):
        self.gv = graphicvisualizer()
        self.z = zwerm(10,self.gv)
        for t in range(1,g_aantalticks):
             self.z.vlieg()
    
    def pressOneTickButton():
        self.z.vlieg()
    
    def __init__(self):
        pass



