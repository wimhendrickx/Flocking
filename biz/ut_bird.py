import unittest
import bird, swarm
from visualinterface import testvisualizer

class Test_Bird(unittest.TestCase):
    def test_init(self):
        tv = testvisualizer()
        s = swarm.swarm(0,tv)
        testvogel = bird.bird(s,tv)
        self.assertTrue(testvogel.getLocation() != None)