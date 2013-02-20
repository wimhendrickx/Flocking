import unittest
import location

g_groottescherm = 400

class Test_Locatie(unittest.TestCase):
    def test_init(self):
        loc = location.location()
        pass

    def test_x_larger_than_0(self):
        loc = location.location()
        self.assertTrue(0 < loc.getX())

    def test_x_smaller_than_scherm(self):
        loc = location.location()
        self.assertTrue(loc.getX() < g_groottescherm)

    def test_y_larger_than_0(self):
        loc = location.location()
        self.assertTrue(0 < loc.getY())

    def test_y_smaller_than_scherm(self):
        loc = location.location()
        self.assertTrue(loc.getY() < g_groottescherm)

    def test_division_x(self):
        setx = float(1)/2
        sety = 1
        loc = location.location(x=setx, y=1)
        self.assertTrue(loc.getX(), 0.5)