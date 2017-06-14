from flask import Flask, request
from twilio import twiml
import helper
 
app = Flask(__name__)
 
 
@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']
    new_message=helper.get_response(message_body)
    resp = twiml.Response()
    resp.message(new_message)
    return str(resp)
if __name__ == '__main__':
	app.run()