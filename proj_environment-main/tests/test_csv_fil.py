import unittest
import csv
import os
import sys

# Legg til src-mappen i path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import finne_mangler

# Sett riktig filsti til CSV-filen (samme som i hente_apidata)
DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'utfylt_data.csv'))


class TestCSV(unittest.TestCase):
    @classmethod #gjør att det kjøres en gang før alle testene
    def setUpClass(cls):
        data_dir = os.path.dirname(DATA_PATH) #
        os.makedirs(data_dir, exist_ok=True) #lager mappen hvis den ikke finnes

    def test_exists(self):
        # Sjekk at filen finnes
        self.assertTrue(os.path.exists(DATA_PATH), f"Filen {DATA_PATH} finnes ikke.")

    def test_csv_header(self):#sjekker headeren i CSV-filen
        with open(DATA_PATH, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            self.assertEqual(header, ['date', 'sunshine_hours'], "CSV-header er feil.") #sjekker at er lik

if __name__ == "__main__":
    unittest.main()
    
'''
Python. (n.d.-a). *Python unittest.* www.python.org. https://docs.python.org/3/library/unittest.html

openAI(n.d.-a). *Chatgpt (GPT-4).* https://chatgpt.com/
'''