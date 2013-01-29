import sys
import unittest

sys.path.append('/Users/Wim/Bird Swarm')
import Test_bird_swarm
import Testintersect

loader = unittest.TestLoader()
suite = loader.loadTestsFromModule(Test_bird_swarm)
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

loader2 = unittest.TestLoader()
suite2 = loader2.loadTestsFromModule(Testintersect)
runner2 = unittest.TextTestRunner(verbosity=2)
result2 = runner2.run(suite2)

#import show_bird_swarm
