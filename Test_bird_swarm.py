from bird_swarm import *
import unittest

class Test_Vogel(unittest.TestCase):
    def test_init(self):
        master = Tk()
        testcanvas = Canvas(master,width=800,height=400)
        testcanvas.pack()
        testvogel = vogel(testcanvas)
        self.assertTrue(testvogel.geeflocatie() != None)
