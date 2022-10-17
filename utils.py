import requests
from dotenv import load_dotenv
import os 
load_dotenv() 

URL = os.getenv("URL")

def sendReq(prompt):
    res = requests.post(f'{URL}/sb/async',)
    