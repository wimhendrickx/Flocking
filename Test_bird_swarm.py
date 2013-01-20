from bird_swarm import *
import unittest

class Test_Vogel(unittest.TestCase):
    def test_init(self):
        master = Tk()
        testcanvas = Canvas(master,width=800,height=400)
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
