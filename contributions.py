import requests
from twilio.rest import TwilioRestClient
import environ
import os
from bs4 import BeautifulSoup
username="simonkrol"
url = 'https://github.com/'+username
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
#print(soup)
#tree = html.fromstring(response.content)
#buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#contributions=tree.xpath('//*[@id="js-pjax-container"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/svg')
#print(contributions)
contributions=[]
for link in soup.find_all('rect'):
    contributions.append(link.get('data-count'))
print(contributions[-1])
environ.set_env()

client = TwilioRestClient(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])

if(contributions[-1]=='0'):
	messageBody="You have yet to make a contribution on Github today. Please do so before midnight or you risk losing your streak."
else:
	messageBody="So far today, you have made "+contributions[-1]+" contributions on Github"
client.messages.create(from_=os.environ['TWILIO_NUMBER'],
					   to=os.environ['MY_NUMBER'],
					   body=messageBody)

