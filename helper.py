from bs4 import BeautifulSoup
import os
from twilio.rest import TwilioRestClient
import requests
import time



def get_contributions(user):
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
		return(user+" has yet to make a contribution on Github today. ")
	elif(cont=="1"):
		return("So far today, "+user+" has made "+cont+" contribution on Github. ")
	else:
		return("So far today, "+user+" has made "+cont+" contributions on Github. ")


def get_streak(user):
	response = requests.get(("https://github.com/"+user))
	soup = BeautifulSoup(response.text, 'lxml')
	soup=soup.find_all('rect')
	if(soup==[]):
		return ("")
	streak=0;
	curr_day=time.strftime("%Y-%m-%d")
	for link in range(len(soup)-1, -1,-1):
		if(soup[link].get('data-date')==curr_day):
			if(soup[link].get('data-count'!="0")):
				streak+=1
			for date in range(link-1, -1, -1):
				if(soup[date].get('data-count')!="0"):
					streak+=1
				else:
					message=user+"'"
					if(user[-1]!="s"):
						message+="s"
					message+= " contribution streak is currently "+str(streak)
					if(streak==1):
						message+=" day."
					else:
						message+=" days."
					return message


def get_help():
	response="Welcome to the github contributions viewer, start your text with the username of the github user you would like to inspect."
	response+=" The second word in your text can be any of the following:"
	response+=" 'contributions'(returns the number of contributions the user has made today), 'streak'(indicates the current contribution streak of the user)."
	response+="\n\n Example: simonkrol streak"
	return response

def get_error(command):
	response=command +" is not a valid command, please send the word 'about' for information on how to use the github contributions viewer."
	return response

def send_sms(message, number):
	client = TwilioRestClient(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])
	client.messages.create(from_=os.environ['TWILIO_NUMBER'],
						   to=number,
						   body=message)