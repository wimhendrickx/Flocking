import unittest
import swarm
from visualinterface import testvisualizer

class Test_Swarm(unittest.TestCase):
    def test_init(self):
        s = swarm.swarm(1, testvisualizer())
        self.assertEqual(s.getNumberOfBirds(), 1)

    def test_getBirds(self):
        s = swarm.swarm(1, testvisualizer())
        self.assertEqual(len(s.getBirds()), 1)

    def test_getCentre_oneBird_x(self):
        s = swarm.swarm(1, testvisualizer())
        bird = s.getBirds()[0]
        x1 = bird.getLocation().geefx()
        self.assertEqual(s.getCentre().getX(), x1)

    def test_getCentre_oneBird_y(self):
        s = swarm.swarm(1, testvisualizer())
        bird = s.getBirds()[0]
        y1 = bird.getLocation().getY()
        self.assertEqual(s.getCentre().getY(), y1)

    def test_getCentre_twoBirds_x(self):
        s = swarm.swarm(2, testvisualizer())
        x1 = s.getBirds()[0].getLocation().getX()
        x2 = s.getBirds()[1].getLocation().getX()
        self.assertEqual(s.getCentre().getX(), (x1+x2)/2)

    def test_getCentre_twoBirds_y(self):
        s = swarm.swarm(2, testvisualizer())
        bird2 = s.getBirds()[1]
        y1 = s.getBirds()[0].getLocation().getY()
        y2 = s.getBirds()[1].getLocation().getY()
        self.assertEqual(s.getCentre().getY(), (y1+y2)/2)

    def test_getCentre_threeBirds_x(self):
        s = swarm.swarm(3, testvisualizer())
        x1 = s.getBirds()[0].getLocation().getX()   
        x2 = s.getBirds()[1].getLocation().getX()
        x3 = s.getBirds()[2].getLocation().getX()
        self.assertEqual(s.getCentre().getX(), (x1+x2+x3)/3)

    def test_getCentre_threeBirds_y(self):
        s = swarm.swarm(3, testvisualizer())
        y1 = s.getBirds()[0].getLocation().getY()
        y2 = s.getBirds()[1].getLocation().getY()
        y3 = s.getBirds()[2].getLocation().getY()
        self.assertEqual(s.getCentre().getY(), (y1+y2+y3)/3)

    def test_getNumberOfBirds(self):
        s = swarm.swarm(1, testvisualizer())
        self.assertEqual(s.getNumberOfBirds(), 1)

    def test_addbird(self):
        s = swarm.swarm(1, testvisualizer())
        s.addbird()
        self.assertEqual(s.getNumberOfBirds(), 2)

    def test_killbird(self):
        t = testvisualizer()
        s = swarm.swarm(1, t)
        s.killbird()
        self.assertEqual(s.getNumberOfBirds(), 0)
        s.killbird()
        self.assertEqual(s.getNumberOfBirds(), 0)

    def test_islocationFree_false(self):
        s = swarm.swarm(1, testvisualizer())
        s.getBirds()[0].getLocation().setX(30)
        s.getBirds()[0].getLocation().setY(40)
        self.assertFalse(s.isLocationFree([30,40]))

    def test_islocationFree_true(self):
        s = swarm.swarm(1, testvisualizer())
        s.getBirds()[0].getLocation().setX(30)
        s.getBirds()[0].getLocation().setY(40)
        self.assertTrue(s.isLocationFree([300,400]))
    
    def test_islocationFree_bothtrue(self):
        s = swarm.swarm(2, testvisualizer())
        s.getBirds()[0].getLocation().setX(30)
        s.getBirds()[0].getLocation().setY(40)
        s.getBirds()[1].getLocation().setX(60)
        s.getBirds()[1].getLocation().setY(80)
        self.assertTrue(s.isLocationFree([45,60]))
    
    def test_islocationFree_onefalse_1(self):
        s = swarm.swarm(2, testvisualizer())
        s.getBirds()[0].getLocation().setX(30)
        s.getBirds()[0].getLocation().setY(40)
        s.getBirds()[1].getLocation().setX(60)
        s.getBirds()[1].getLocation().setY(80)
        self.assertFalse(s.isLocationFree([31,41]))
        
    def test_islocationFree_onefalse_2(self):
        s = swarm.swarm(2, testvisualizer())
        s.getBirds()[0].getLocation().setX(30)
        s.getBirds()[0].getLocation().setY(40)
        s.getBirds()[1].getLocation().setX(60)
        s.getBirds()[1].getLocation().setY(80)
        self.assertFalse(s.isLocationFree([31,41]))
    
    def test_islocationFree_onefalse_2(self):
        s = swarm.swarm(2, testvisualizer())
        s.getBirds()[0].getLocation().setX(30)
        s.getBirds()[0].getLocation().setY(40)
        s.getBirds()[1].getLocation().setX(60)
        s.getBirds()[1].getLocation().setY(80)
        self.assertFalse(s.isLocationFree([32,42]))
        
    def test_islocationFree_onefalse_3(self):
        s = swarm.swarm(2, testvisualizer())
        s.getBirds()[0].getLocation().setX(30)
        s.getBirds()[0].getLocation().setY(40)
        s.getBirds()[1].getLocation().setX(60)
        s.getBirds()[1].getLocation().setY(80)
        self.assertFalse(s.isLocationFree([33,43]))
        
        
    def test_islocationFree_onefalse_4(self):
        s = swarm.swarm(2, testvisualizer())
        s.getBirds()[0].getLocation().setX(30)
        s.getBirds()[0].getLocation().setY(40)
        s.getBirds()[1].getLocation().setX(60)
        s.getBirds()[1].getLocation().setY(80)
        self.assertFalse(s.isLocationFree([34,44]))

    def test_islocationFree_onefalse_5(self):
        s = swarm.swarm(2, testvisualizer())
        s.getBirds()[0].getLocation().setX(30)
        s.getBirds()[0].getLocation().setY(40)
        s.getBirds()[1].getLocation().setX(60)
        s.getBirds()[1].getLocation().setY(80)
        #De afstand van kern tot kern is 7,07 en dit is groter als 2* de straal van de bird (2*3=6)
        self.assertTrue(s.isLocationFree([35,45]))
