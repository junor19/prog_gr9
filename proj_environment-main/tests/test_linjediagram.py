import unittest
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
from unittest.mock import patch

# Legg til src-mappen i path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import linjediagram
from linjediagram import laste_data, lage_graf

class TestLinjediagram(unittest.TestCase):
    def setUp(self):
        self.test_data = pd.DataFrame({
            'date': ['2020-05-05', '2020-05-06'],
            'solskinnstimer': [5, 6]
        })
        
        self.test_dir = os.path.dirname(__file__)  # mappen der testfilen ligger
        self.testfile = os.path.join(self.test_dir, "testdata.csv") #lager en midlertidig filsti i testmappen
        self.test_data.to_csv(self.testfile, index=False) #denne linjen lager en CSV-fil med testdata
        
    def tearDown(self):
        if os.path.exists(self.testfile):
            os.remove(self.testfile)    #fjerner testfilen etter at testen er kjørt
            
    def test_data(self):
            
        self.assertIn('date', self.test_data.columns)
        self.assertIn('solskinnstimer', self.test_data.columns)
        
    def test_lage_graf(self):
        df = self.test_data.copy()
        df = df.rename(columns={'solskinnstimer': 'sunshine_hours'})
        df['date'] = pd.to_datetime(df['date']) #konverterer datoen til datetime format
        df['year'] = df['date'].dt.year #henter ut året fra datoen og legger i egen kolonne
        df['day_month'] = df['date'].dt.strftime('%m-%d') #henter ut dag og måned fra datoen og legger i egen kolonne
        
        with patch('matplotlib.pyplot.show'):
            pivot_df = lage_graf(df)
        
        self.assertTrue(isinstance(pivot_df, pd.DataFrame))
        
if __name__ == '__main__':
    unittest.main()