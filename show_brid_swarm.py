#!/usr/bin/python
import bird_swarm
from Tkinter import *

#GLOBALVARS
g_aantalvogels = 3
g_groottescherm = 600
g_groottevogel = 6
g_flapperafstand = 50
g_aantalticks = 10

master = Tk()
z = bird_swarm.zwerm(g_aantalvogels,master)
#z.bepaalmidden()

for t in range(1,g_aantalticks):
    print('ronde')
    print(t)
    z.vlieg()
#    time.sleep(0.50)
#master.mainloop()
