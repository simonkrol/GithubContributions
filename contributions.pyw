import requests
from twilio.rest import TwilioRestClient
import environ#File used to set environment variables
import os
from bs4 import BeautifulSoup
import schedule
import time


username='simonkrol'
send_time="22:00"


url = 'https://github.com/'+username
def get_cont():
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'lxml')

	# contributions=[]
	# for link in soup.find_all('rect'): #Gets a list of contribution numbers for each day 
	#     contributions.append(link.get('data-count')) 
	#print(contributions[-1])
	curr_day=time.strftime("%Y-%m-%d")
	curr_div=soup.find_all('rect')[-1]
	if(curr_div.get('data-date')!=curr_day):
		curr_div=soup.find_all('rect')[-2]
	return(curr_div.get('data-count'))


def send_sms(cont):
	client = TwilioRestClient(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])

	if(cont=='0'):
		messageBody=username+" has yet to make a contribution on Github today."
	else:
		messageBody="So far today,"+username+" has made "+cont+" contributions on Github"
	client.messages.create(from_=os.environ['TWILIO_NUMBER'],
						   to=os.environ['MY_NUMBER'],
						   body=messageBody)
def run():
	environ.set_env()
	send_sms(get_cont())

run()
schedule.every().day.at(send_time).do(run)
while True:
	schedule.run_pending()
	time.sleep(60)