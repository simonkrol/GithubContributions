from flask import Flask, request
from twilio import twiml
import contributions
 
app = Flask(__name__)
 
 
# @app.route('/sms', methods=['POST'])
# def sms():
# 	number = request.form['From']
# 	message_body = request.form['Body']
# 	cont=contributions.get_cont(message_body)
# 	message=contributions.get_message(cont)
# 	resp = twiml.Response()
# 	resp.message(message)
# 	return str(resp)
@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']
 
    resp = twiml.Response()
    resp.message('Hello {}, you said: {}'.format(number, message_body))
    return str(resp)
if __name__ == '__main__':
	app.run()