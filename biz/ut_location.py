import unittest
import location

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
        loc = locatie(x=setx, y=1)
        self.assertTrue(loc.geefx(), 0.5)