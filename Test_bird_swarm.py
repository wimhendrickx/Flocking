from bird_swarm import *
import unittest

class Test_Vogel(unittest.TestCase):
    def test_init(self):
##        testcanvas = Canvas(Tk(),width=800,height=400)
##        testcanvas.pack()
        testvogel = vogel(testvisualizer())
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

    def test_division_x(self):
        setx = float(1)/2
	sety = 1
	print setx
        loc = locatie(x=setx, y=1)
	self.assertTrue(loc.geefx(), 0.5)

class Test_Zwerm(unittest.TestCase):
    def test_init(self):
        zw = zwerm(1, testvisualizer())
        self.assertEqual(zw.geefaantalvogels(), 1)

    def test_getVogels(self):
        zw = zwerm(1, testvisualizer())
        self.assertEqual(len(zw.geefvogels()), 1)

    def test_geefmidden_oneBird_x(self):
        zw = zwerm(1, testvisualizer())
        vogel = zw.geefvogels()[0]
        x1 = vogel.geeflocatie().geefx()
        self.assertEqual(zw.geefmidden().geefx(), x1)

    def test_geefmidden_oneBird_y(self):
        zw = zwerm(1, testvisualizer())
        vogel = zw.geefvogels()[0]
        y1 = vogel.geeflocatie().geefy()
        self.assertEqual(zw.geefmidden().geefy(), y1)

    def test_geefmidden_twoBirds_x(self):
        zw = zwerm(2, testvisualizer())
	x1 = zw.geefvogels()[0].geeflocatie().geefx()
	x2 = zw.geefvogels()[1].geeflocatie().geefx()
        self.assertEqual(zw.geefmidden().geefx(), (x1+x2)/2)

    def test_geefmidden_twoBirds_y(self):
        zw = zwerm(2, testvisualizer())
        vogel2 = zw.geefvogels()[1]
	y1 = zw.geefvogels()[0].geeflocatie().geefy()
	y2 = zw.geefvogels()[1].geeflocatie().geefy()
        self.assertEqual(zw.geefmidden().geefy(), (y1+y2)/2)

    def test_geefmidden_threeBirds_x(self):
        zw = zwerm(3, testvisualizer())
	x1 = zw.geefvogels()[0].geeflocatie().geefx()
	x2 = zw.geefvogels()[1].geeflocatie().geefx()
	x3 = zw.geefvogels()[2].geeflocatie().geefx()
        self.assertEqual(zw.geefmidden().geefx(), (x1+x2+x3)/3)

    def test_geefmidden_threeBirds_y(self):
        zw = zwerm(3, testvisualizer())
	y1 = zw.geefvogels()[0].geeflocatie().geefy()
	y2 = zw.geefvogels()[1].geeflocatie().geefy()
	y3 = zw.geefvogels()[2].geeflocatie().geefy()
        self.assertEqual(zw.geefmidden().geefy(), (y1+y2+y3)/3)

    def test_geefaantalvogel(self):
        zw = zwerm(1, testvisualizer())
        self.assertEqual(zw.geefaantalvogels(), 1)

    def test_addbird(self):
        zw = zwerm(1, testvisualizer())
        zw.addbird()
        self.assertEqual(zw.geefaantalvogels(), 2)

    def test_killbird(self):
        zw = zwerm(1, testvisualizer())
        zw.killbird()
        self.assertEqual(zw.geefaantalvogels(), 0)
        zw.killbird()
        self.assertEqual(zw.geefaantalvogels(), 0)
        
