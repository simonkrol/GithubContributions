import requests
from twilio.rest import TwilioRestClient
import environ#File used to set environment variables
import os
from bs4 import BeautifulSoup
username='cbkrol'
url = 'https://github.com/'+username
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# contributions=[]
# for link in soup.find_all('rect'): #Gets a list of contribution numbers for each day 
#     contributions.append(link.get('data-count')) 
#print(contributions[-1])
cont=(soup.find_all('rect')[-1]).get('data-count')
environ.set_env()

client = TwilioRestClient(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])

if(cont=='0'):
	messageBody=username+" has yet to make a contribution on Github today."
else:
	messageBody="So far today,"+username+" has made "+cont+" contributions on Github"
client.messages.create(from_=os.environ['TWILIO_NUMBER'],
					   to=os.environ['MY_NUMBER'],
					   body=messageBody)

