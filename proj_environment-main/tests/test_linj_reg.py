import unittest
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import os
from unittest.mock import patch
from datetime import datetime

# Legg til src-mappen i path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import linjaer_reg
from linjaer_reg import forbred_data, tren_pred, gen_framtid, vis_fremtid

class TestLinjaerReg(unittest.TestCase):
    def setUp(self): #lager en dataframe for testing
        self.test_data = pd.DataFrame({
            'date': ['2020-05-05', '2020-05-06'],
            'sunshine_hours': [5, 6]
        })
        # konverterer datoen til datetime format
        self.test_file = 'test_forbred_data.csv'
        self.test_data.to_csv(self.test_file, index=False)
         
    
    def tearDown(self):
        # Sletter testfilen etter testen
        if os.path.exists(self.test_file):
            os.remove(self.test_file)    #fjerner testfilen etter at testen er kjørt
            
    def test_sin(self):
        df,x, y = forbred_data(self.test_file) #forbereder data
        self.assertIn('sin_day', df.columns) #sjekker at sin_day kolonnen er i df
        
    def test_koef(self):
        df, x, y = forbred_data(self.test_file) #forbereder data
        #modell, y_pred = tren_pred(df, x, y) # trener modellen
        
        with patch('matplotlib.pyplot.show'): # hindrer at grafen vises under testen
            modell, y_pred = tren_pred(df, x, y)
            
        coeffs = modell.coef_   
        self.assertEqual(len(coeffs), 2) #sjekker at koeffisient er 2
        
    def test_len_fremtid(self):
        startdato = datetime(2020, 5, 5) # starter fra 5. mai 2020
        antall_dager = 10 # antall dager frem i tid
        df_framtid = gen_framtid(startdato, antall_dager) # genererer fremtidige datoer
        self.assertEqual(len(df_framtid), antall_dager) #sjekker at lengden på df_framtid er lik antall dager
        
if __name__ == '__main__':
    unittest.main()
    
'''
Python. (n.d.-a). *Python unittest.* www.python.org. https://docs.python.org/3/library/unittest.html

openAI(n.d.-a). *Chatgpt (GPT-4).* https://chatgpt.com/
'''