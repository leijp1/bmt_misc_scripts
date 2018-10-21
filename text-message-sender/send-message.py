from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACb223151d04e273066d62a711d9c9ddb0'
auth_token = '5318c0bbb2c021b34f8b80d1cb6f711b'
client = Client(account_sid, auth_token)

#list of phone numbers
phone_numbers_from = ['+15109014758'] 
phone_numbers_message_count = [0 for _ in range(len(phone_numbers_from))] #make it so that this thing is saved after every function call
#refactor above as dictionaries

phone_numbers_to = [] #write function to collect all phone numbers from a spreadsheet
phone_numbers_to_test = ["+16305064914", "+13052816436"]

#max number of messages send from phone number
PHONE_NUMBER_MAX = 250



def send_message(message, is_test=False):

	index = 0
	messages_sent_count = 0
	if(is_test):
		phone_numbers_to = phone_numbers_to_test

	while messages_sent_count < len(phone_numbers_to):
		send_message_specifying_phone_numbers(message, phone_numbers_to[messages_sent_count], phone_numbers_from[index])
		phone_numbers_message_count[index] += 1
		messages_sent_count+= 1
		if(phone_numbers_message_count[index] % PHONE_NUMBER_MAX == 0):
			index+=1
		if index >= len(phone_numbers_from):
			raise Exception("Error Not Enough Numbers to Send All Phone Messages. Add more numbers")
	print("All Messages Sent Successfully")



def clear_phone_numbers_from():
	phone_numbers_from = []









def send_message_specifying_phone_numbers(message, phone_number_to, phone_number_from):
	print(phone_number_to)
	message = client.messages \
                .create(
                     body= message,
                     from_= phone_number_from,
                     to= phone_number_to
                 )
	