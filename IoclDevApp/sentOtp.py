from twilio.rest import Client
class Smsclass():
    def send_sms_twillio(to_number, otp):
        
        # Set environment variables 
        account_sid = "AC58ce0fab20dfaf93cb9c50e13b068441"
        auth_token = "73e360b56e4f4cf54ee9f0ff17e380b0"
        client = Client(account_sid, auth_token)

        message = "Your OTP for hosepipe is " + otp

        message = client.messages.create(
            body = message,
            from_ = "+12067016270",
            to = "+91" + to_number
        )