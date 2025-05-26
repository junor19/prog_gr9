import unittest
import pandas as pd
import sys
import os

# Legg til src-mappen i path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import finne_mangler
from finne_mangler import finne_hull

class test_finne_hull(unittest.TestCase):
    def setUp(self): #laget en testdata som skal brukes i testen
        self.test = pd.DataFrame({
            'date': ['2023-01-01', '2023-01-02', '2023-01-04', '2023-01-04'],
            'sunshine_hours': [5, 6, 7, 7]
        })
        test_dir = os.path.dirname(__file__)  # mappen der testfilen ligger
        self.testfile = os.path.join(test_dir, "testdata_temp.csv") #lager en midlertidig filsti i testmappen
        
        self.test.to_csv(self.testfile, index=False) #denne linjen lager en CSV-fil med testdata
        
    def tearDown(self):
        if os.path.exists(self.testfile):
            os.remove(self.testfile)    #fjerner testfilen etter at testen er kjørt
    
    def test_finne_hull(self):
        duplikater, manglende_datoer = finne_hull(self.testfile, 'date') #kobler til funksjonen som skal testes
        self.assertEqual(len(duplikater), 1) #sjekker at det er 1 duplikat
        self.assertEqual(len(manglende_datoer), 1) #sjekker at det er 1 manglende dato

if __name__ == '__main__':
    unittest.main()