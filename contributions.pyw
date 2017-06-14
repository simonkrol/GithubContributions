import requests
from twilio.rest import TwilioRestClient
import environ#File used to set environment variables
import os
from bs4 import BeautifulSoup
import schedule
import time


username='simonkrol'
send_time="22:00"


url = 'https://github.com/'
def get_cont(user):
	response = requests.get((url+user))
	soup = BeautifulSoup(response.text, 'lxml')
	soup=soup.find_all('rect')
	curr_day=time.strftime("%Y-%m-%d")
	for link in range(len(soup)-1, -1,-1):
		if(soup[link].get('data-date')==curr_day):
			return soup[link].get('data-count')

def get_message(cont):
	if(cont=='0'):
		return(username+" has yet to make a contribution on Github today.")
	else:
		return("So far today, "+username+" has made "+cont+" contributions on Github")
def send_sms(cont):
	client = TwilioRestClient(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])
	client.messages.create(from_=os.environ['TWILIO_NUMBER'],
						   to=os.environ['MY_NUMBER'],
						   body=get_message(cont))
def run():
	environ.set_env()
	send_sms(get_cont(username))
#run()#Uncomment to test sms functionality

schedule.every().day.at(send_time).do(run)
while True:
	schedule.run_pending()
	time.sleep(60)