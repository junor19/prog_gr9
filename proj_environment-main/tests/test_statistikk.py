import unittest
import pandas as pd
import sys
import os

import median_osv
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from median_osv import statistikk

class test_statistikk(unittest.TestCase):
    def setUp(self):
        self.filnavn = 'testdata.csv'
        self.kolonnenavn = 'verdier'
        self.data = pd.DataFrame({
            self.kolonnenavn: [1, 3, 5, 7, 9]  # Median = 5, Gj.snitt = 5, Std.avvik ≈ 3.16
        })
        self.data.to_csv(self.filnavn, index=False)

    def tearDown(self):
        os.remove(self.filnavn)
    
    def test_median(self):
        median, _, _ = statistikk(self.test_fil)
        self.assertEqual(median[self.kolonnenavn], 5)
        
    def test_gjennomsnitt(self):
        _, gjennomsnitt, _ = statistikk(self.test_fil)
        self.assertNotEqual(gjennomsnitt[self.kolonnenavn], 9)
        
    def test_standardavvik(self):
        _, _, standardavvik = statistikk(self.test_fil)
        self.assertNotEqual(standardavvik[self.kolonnenavn], 0)
        
    
        
if __name__ == "__main__":
    unittest.main()