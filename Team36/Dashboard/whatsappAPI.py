from twilio.rest import Client

 def send_message():
	account_sid = 'AC781521c715930fdabb7359aee7138a85' 
	auth_token = '29623369c9a7ab226f518ad5aeeb3e3c' 
	client = Client(account_sid, auth_token) 
 
	message = client.messages.create( 
								from_='whatsapp:+14155238886',  
								body='Your Yummy Cupcakes Company order of 1 dozen frosted cupcakes has shipped and should be delivered on July 10, 2019. Details: http://www.yummycupcakes.com/',      
								to='whatsapp:+919867416562' 
							) 
 
	print(message.sid)