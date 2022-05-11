from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client

account_sid = "twilio-sid"
auth_token = "twilio-token"


phoneno = 'your-virtual-twillo-no'
target = 'target-phone-numer'


myphone = Client(account_sid, auth_token)

def notify():
    try :
        call = myphone.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to= target,
                        from_= phoneno
                )

    except TwilioRestException as err:
        print(err)
    print(call.sid)




