from bird_swarm import *
import unittest



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

    def test_islocationFree_false(self):
        zw = zwerm(1, testvisualizer())
        zw.geefvogels()[0].geeflocatie().zetx(30)
        zw.geefvogels()[0].geeflocatie().zety(40)
        self.assertFalse(zw.isLocationFree([30,40]))

    def test_islocationFree_true(self):
        zw = zwerm(1, testvisualizer())
        zw.geefvogels()[0].geeflocatie().zetx(30)
        zw.geefvogels()[0].geeflocatie().zety(40)
        self.assertTrue(zw.isLocationFree([300,400]))
    
    def test_islocationFree_bothtrue(self):
        zw = zwerm(2, testvisualizer())
        zw.geefvogels()[0].geeflocatie().zetx(30)
        zw.geefvogels()[0].geeflocatie().zety(40)
        zw.geefvogels()[1].geeflocatie().zetx(60)
        zw.geefvogels()[1].geeflocatie().zety(80)
        self.assertTrue(zw.isLocationFree([45,60]))
    
    def test_islocationFree_onefalse_1(self):
        zw = zwerm(2, testvisualizer())
        zw.geefvogels()[0].geeflocatie().zetx(30)
        zw.geefvogels()[0].geeflocatie().zety(40)
        zw.geefvogels()[1].geeflocatie().zetx(60)
        zw.geefvogels()[1].geeflocatie().zety(80)
        self.assertFalse(zw.isLocationFree([31,41]))
        
    def test_islocationFree_onefalse_2(self):
        zw = zwerm(2, testvisualizer())
        zw.geefvogels()[0].geeflocatie().zetx(30)
        zw.geefvogels()[0].geeflocatie().zety(40)
        zw.geefvogels()[1].geeflocatie().zetx(60)
        zw.geefvogels()[1].geeflocatie().zety(80)
        self.assertFalse(zw.isLocationFree([31,41]))
    
    def test_islocationFree_onefalse_2(self):
        zw = zwerm(2, testvisualizer())
        zw.geefvogels()[0].geeflocatie().zetx(30)
        zw.geefvogels()[0].geeflocatie().zety(40)
        zw.geefvogels()[1].geeflocatie().zetx(60)
        zw.geefvogels()[1].geeflocatie().zety(80)
        self.assertFalse(zw.isLocationFree([32,42]))
        
    def test_islocationFree_onefalse_3(self):
        zw = zwerm(2, testvisualizer())
        zw.geefvogels()[0].geeflocatie().zetx(30)
        zw.geefvogels()[0].geeflocatie().zety(40)
        zw.geefvogels()[1].geeflocatie().zetx(60)
        zw.geefvogels()[1].geeflocatie().zety(80)
        self.assertFalse(zw.isLocationFree([33,43]))
        
        
    def test_islocationFree_onefalse_4(self):
        zw = zwerm(2, testvisualizer())
        zw.geefvogels()[0].geeflocatie().zetx(30)
        zw.geefvogels()[0].geeflocatie().zety(40)
        zw.geefvogels()[1].geeflocatie().zetx(60)
        zw.geefvogels()[1].geeflocatie().zety(80)
        self.assertFalse(zw.isLocationFree([34,44]))

    def test_islocationFree_onefalse_5(self):
        zw = zwerm(2, testvisualizer())
        zw.geefvogels()[0].geeflocatie().zetx(30)
        zw.geefvogels()[0].geeflocatie().zety(40)
        zw.geefvogels()[1].geeflocatie().zetx(60)
        zw.geefvogels()[1].geeflocatie().zety(80)
        #De afstand van kern tot kern is 7,07 en dit is groter als 2* de straal van de vogel (2*3=6)
        self.assertTrue(zw.isLocationFree([35,45]))