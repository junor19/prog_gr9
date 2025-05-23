import unittest
import csv
import os
import sys

# Legg til src-mappen i path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import hente_apidata

# Sett riktig filsti til CSV-filen (samme som i hente_apidata)
DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'raa_data_d.csv'))


class TestCSV(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        data_dir = os.path.dirname(DATA_PATH)
        os.makedirs(data_dir, exist_ok=True)
        # Kjør API-kall én gang før alle testene
        hente_apidata.hent_solskinnstimer("t_månder", "tjue", "raa_data_d.csv")

    def test_exists(self):
        
        self.assertTrue(os.path.exists(DATA_PATH), f"Filen {DATA_PATH} finnes ikke.")

    def test_csv_header(self):
        with open(DATA_PATH, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            self.assertEqual(header, ['date', 'sunshine_hours'], "CSV-header er feil.")

if __name__ == "__main__":
    unittest.main()
    