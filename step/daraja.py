import requests
import datetime
import base64
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from erp import settings

def get_access_token():
    consumer_key = settings.CONSUMER_KEY
    consumer_secret = settings.CONSUMER_SECRET
    url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    
    response = requests.get(url, auth=(consumer_key, consumer_secret))
    if response.status_code == 200:
        token = response.json()['access_token']
        return token
    else:
        raise Exception("Failed to get access token")

def generate_password(shortcode, passkey, timestamp):
    concatenated_string = f"{shortcode}{passkey}{timestamp}"
    password = base64.b64encode(concatenated_string.encode()).decode('utf-8')
    return password

def initiate_stk_push():
    phone_number = 254700445982
    amount = 10
    
   
    shortcode =  174379
    passkey = settings.DARAJA_PASSKEY
   

    # Generate the timestamp and password
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    password = generate_password(shortcode, passkey, timestamp)
    
    # Get access token
    
    token = get_access_token()
   
       

    # Set headers and payload
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "BusinessShortCode": shortcode,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": shortcode,
        "PhoneNumber": phone_number,
        "CallBackURL": "https://mydomain.com/path",
        "AccountReference": "AWK SOFTWARES",
        "TransactionDesc": "Payment for goods/services"
    }

    # Debugging: print payload to verify structure
    print("Payload:", payload)

    # Send the request to Daraja API
    stk_push_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    response = requests.post(stk_push_url, json=payload, headers=headers)

    # Debugging: print response to verify result
    print("Response Status Code:", response.status_code)
    print("Response Content:", response.json())

    # Process the response
    context = {
        "success": response.status_code == 200,
        "status_code": response.status_code,
        "response": response.json()
    }
    print(context)




