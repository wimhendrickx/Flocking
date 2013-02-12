import sys
import unittest

g_groottescherm = 400

sys.path.append('/Users/Wim/Flocking')
sys.path.append('/Users/Wim/Flocking/int')

import ut_bird

loader = unittest.TestLoader()
suite = loader.loadTestsFromModule(ut_bird)
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

# loader2 = unittest.TestLoader()
# suite2 = loader2.loadTestsFromModule(Testintersect)
# runner2 = unittest.TextTestRunner(verbosity=2)
# result2 = runner2.run(suite2)