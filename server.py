from flask import Flask, request
from twilio import twiml
import helper
 
app = Flask(__name__)
 
 
@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']
    body=message_body.split()
    print(body)
    new_message=helper.get_response(body[0])
    streak_message=""
    if(len(body)>1):
    	if(body[1].lower()=="streak"):
    		streak_message=helper.get_streak(body[0])
    resp = twiml.Response()
    new_message=new_message+streak_message
    resp.message(new_message)
    return str(resp)
if __name__ == '__main__':
	app.run()