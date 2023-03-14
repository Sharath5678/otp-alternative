import os 
from twilio.rest import Client


account_sid = 'AC877bc7976215da7dc6ef1df24ee8e91a'
auth_token = 'cd9a315be5056c60c4b7030e9dbce872'
client = Client(account_sid,auth_token)

def send_sms(user_code,phone_number):
    messages = client.messages.create(
        body = f' Hey lad, your Username and Verification is {user_code} ',
        from_ = '+17262007184',
        to=f'{phone_number}'
    )
    print(messages.sid)