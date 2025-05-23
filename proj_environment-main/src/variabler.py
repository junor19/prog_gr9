#API-nøkkel som bør ligge i et annet doc
client_id = "bd3f25c0-324e-4a26-a507-5887be8b3c9d"

''' fra 
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
api_key = os.getenv('API_KEY')

if api_key is None:
    raise ValueError("API key not found in environment variables.")
    
'''

#variablene
stasjon_id = "SN68173"  #stasjons-id for gløs

elementer = {
    "t_dager": "sum(duration_of_sunshine P1D)",  #hvor mange timer med sol det har vært i døgnet.
}
    
tidsperioder = {
    "seksten": "2016-01-01/2021-01-01",  #for stasjon gløshaugen var det tilgjengelig data fra og med 2016, så det er der vi startet
}