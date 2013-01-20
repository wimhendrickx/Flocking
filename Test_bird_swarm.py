from bird_swarm import *
import unittest

class Test_Vogel(unittest.TestCase):
    def test_init(self):
        testcanvas = Canvas(Tk(),width=800,height=400)
        testcanvas.pack()
        testvogel = vogel(testcanvas)
        self.assertTrue(testvogel.geeflocatie() != None)

class Test_Locatie(unittest.TestCase):
    g_groottescherm = 400
    def test_init(self):
        loc = locatie()
        pass

    def test_x_larger_than_0(self):
        loc = locatie()
        self.assertTrue(0 < loc.geefx())

    def test_x_smaller_than_scherm(self):
        loc = locatie()
        self.assertTrue(loc.geefx() < g_groottescherm)

    def test_y_larger_than_0(self):
        loc = locatie()
        self.assertTrue(0 < loc.geefy())

    def test_y_smaller_than_scherm(self):
        loc = locatie()
        self.assertTrue(loc.geefy() < g_groottescherm)

class Test_Zwerm(unittest.TestCase):
    def test_init(self):
        zw = zwerm(1, Tk())
        self.assertEqual(zw.geefaantalvogels(), 1)

    def test_getVogels(self):
        zw = zwerm(1, Tk())
        self.assertEqual(len(zw.geefvogels()), 1)

    def test_geefmidden(self):
        zw = zwerm(1, Tk())
        vogel = zw.geefvogels()[0]
        x1 = vogel.geeflocatie().geefx()
        y1 = vogel.geeflocatie().geefy()
        self.assertEqual(zw.geefmidden().geefx(), x1)
        self.assertEqual(zw.geefmidden().geefy(), y1)
        zw.addbird()
        vogel2 = zw.geefvogels()[1]
        x2 = vogel2.geeflocatie().geefx()
        y2 = vogel2.geeflocatie().geefy()
        self.assertEqual(zw.geefmidden().geefx(), (x1+x2)/2)
        self.assertEqual(zw.geefmidden().geefy(), (y1+y2)/2)
        zw.addbird()
        vogel3 = zw.geefvogels()[2]
        x3 = vogel3.geeflocatie().geefx()
        y3 = vogel3.geeflocatie().geefy()
        self.assertEqual(zw.geefmidden().geefx(), (x1+x2+x3)/3)
        self.assertEqual(zw.geefmidden().geefy(), (y1+y2+y3)/3)

    def test_geefaantalvogel(self):
        zw = zwerm(1, Tk())
        self.assertEqual(zw.geefaantalvogels(), 1)

    def test_addbird(self):
        zw = zwerm(1, Tk())
        zw.addbird()
        self.assertEqual(zw.geefaantalvogels(), 2)

    def test_killbird(self):
        zw = zwerm(1, Tk())
        zw.killbird()
        self.assertEqual(zw.geefaantalvogels(), 0)
        zw.killbird()
        self.assertEqual(zw.geefaantalvogels(), 0)
        
