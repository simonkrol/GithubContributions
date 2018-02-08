from flask import Flask, request
from twilio import twiml
import helper
 
app = Flask(__name__)
 
#Set method call location on /sms post request
@app.route('/sms', methods=['POST'])

def sms():
    number = request.form['From']
    message_body = request.form['Body']
    body=message_body.split()
    body.append("error")

    #Generate the correct response based on user's message
    message= {
    	'about': "helper.get_help()",
    	'today': "helper.get_contributions(body[0])",
        'streak': "helper.get_streak(body[0])",
        'total': "helper.get_total(body[0])"
    }.get(body[-2].lower(), "helper.get_error(body[-2])")
    message=eval(message)
    #Check for help
    if(body[0]=="help"):
    	message=helper.get_help()

    #Generate Twilio Response
    resp = twiml.Response()
    #Respond to SMS
    resp.message(message)
    return str(resp)

if __name__ == '__main__':
	app.run() #Start the flask app