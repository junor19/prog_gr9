import unittest 
import csv
from datetime import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../src')))

import hente_apidata

class testmonth(unittest.TestCase):
    def test_date(self):
        #with open(raa_data_d.csv, 'r') as csvfile:
         #   reader = csv.reader(csvfile)
          #  for row in reader:
           #     date = datetime.strptime(date_string,"2020-01-01")
        year = 
        forventet_dato = datetime(2020,10,10)
        self.assertIn(forventet_dato, hente_apidata)
        
if __name__ == "__main__":
    unittest.main()