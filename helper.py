from bs4 import BeautifulSoup
import requests
import time



def get_response(user):
	response = requests.get(("https://github.com/"+user))
	soup = BeautifulSoup(response.text, 'lxml')
	soup=soup.find_all('rect')
	if(soup==[]):
		return (user+" is not a GitHub user.")
	curr_day=time.strftime("%Y-%m-%d")
	for link in range(len(soup)-1, -1,-1):
		if(soup[link].get('data-date')==curr_day):
			return get_message(soup[link].get('data-count'), user)

def get_message(cont, user):
	if(cont=='0'):
		return(user+" has yet to make a contribution on Github today.")
	else:
		return("So far today, "+user+" has made "+cont+" contributions on Github")


def send_sms(message, number):
	client = TwilioRestClient(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])
	client.messages.create(from_=os.environ['TWILIO_NUMBER'],
						   to=number,
						   body=message)