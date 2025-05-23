import unittest
import pandas as pd
import sys
import os

import median_osv
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from median_osv import statistikk

class test_statistikk(unittest.TestCase):
    def median_test(self):
        forventet_median, _, _ = statistikk(self.test_fil)
        ikke_rett_median = 5
        self.assertNotEqual(forventet_median,ikke_rett_median)

if __name__ == "__main__":
    unittest.main()