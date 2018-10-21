from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACb223151d04e273066d62a711d9c9ddb0'
auth_token = '5318c0bbb2c021b34f8b80d1cb6f711b'
client = Client(account_sid, auth_token)



def send_message(message, phone_number_to):
    print(phone_number_to)
    message = client.messages \
                .create(
                     body= message,
                     messaging_service_sid='MGdf019ebed3e609d274cc66aaffb0d2e3',
                     to= phone_number_to
                 )


