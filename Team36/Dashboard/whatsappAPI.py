from twilio.rest import Client

def send_message():
    account_sid = 'AC781521c715930fdabb7359aee7138a85' 
    auth_token = '29623369c9a7ab226f518ad5aeeb3e3c' 
    client = Client(account_sid, auth_token) 

    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body = 'Please Click here to access your quarterly report: https://drive.google.com/file/d/17zYDF0K8A9EdGEp8169iYVviCR2KbJDo/view?usp=sharing',
                                #body='Click Here http://localhost:8000/dashboard/pdf/',      
                                to='whatsapp:+919867416562' 
                            ) 

    print(message.sid)