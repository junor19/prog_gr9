import unittest
import pandas as pd
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import sentralmal
from sentralmal import statistikk

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
    
    def test_median(self): #sjekker at median funksjonen fungerer
        median, _, _ = statistikk(self.filnavn)
        self.assertEqual(median[self.kolonnenavn], 5)
        
    def test_gjennomsnitt(self): #sjekker at gjennomsnitt funksjonen fungerer
        _, gjennomsnitt, _ = statistikk(self.filnavn)
        self.assertNotEqual(gjennomsnitt[self.kolonnenavn], 9)
        
    def test_standardavvik(self): #sjekker at standardavvik funksjonen fungerer
        _, _, standardavvik = statistikk(self.filnavn)
        self.assertNotEqual(standardavvik[self.kolonnenavn], 0)
        
    
        
if __name__ == "__main__":
    unittest.main()