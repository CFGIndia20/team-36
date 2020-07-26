from twilio.rest import Client

account_sid = 'XXXXX'
auth_token = 'XXXXX'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Welcome to CFG India 2020 !",
                     from_='+13392349976',
                     to='<your-number>'
                 )

print(message.sid)