import requests
from requests.auth import HTTPBasicAuth
import json





def get_access_token():
    consumer_key = 'lh3qBHBMlINl1QCyQsMAmAwT6JiEVA8Co5yXv6ea6NZpAWbo'
    consumer_secret = 'NtU6W1AFHOK7o5SHjd1Q7zybuJ7njCtSFCNpRLAjYGjj9dyGC3s6nr1xXCiteY57'
    url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    response = requests.get(url,  auth=HTTPBasicAuth(consumer_key, consumer_secret))
    
    if response.status_code == 200:
        token = json.loads(response.text)
        access_token = token['access_token']
        return access_token
  

x=get_access_token()
print(x)