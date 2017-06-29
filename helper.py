from bs4 import BeautifulSoup
import os
from twilio.rest import TwilioRestClient
import requests
import time


#Finds the number of contributions a user has made today
def get_contributions(user):
	response = requests.get(("https://github.com/"+user)) #Recieve the response from the webpage
	soup = BeautifulSoup(response.text, 'lxml')	#Parse into lxml
	soup=soup.find_all('rect')	#Find all 'rect tags'
	if(soup==[]):	#Make sure given username exists
		return (user+" is not a GitHub user.")
	curr_day=time.strftime("%Y-%m-%d")
	print(curr_day) #Log the date for debugging
	for link in range(len(soup)-1, -1,-1):	#Check all tags until we find the correct date, starting from the most recent
		if(soup[link].get('data-date')==curr_day):
			return get_message(soup[link].get('data-count'), user) #Return a message containing the number of contributions

#Finds the number of contributions a user has made in the past year
#Since Github calculates this for us, we simply take the calculate number from the page
def get_total(user):
	response=requests.get(("https://github.com/"+user))
	soup=BeautifulSoup(response.text, 'lxml')
	soup=soup.find_all('h2', { "class" : "f4 text-normal mb-2"}) #Find all h2 elements with the f4 text-normal mb-2 class
	for h2 in soup:
		total_cont=(h2.get_text().split(' '))[6]	#Get the desired piece of information
		response=user +" has made "+total_cont + " contributions in the past year."
		return response

#Returns a message representing the number of contributions a user has made
def get_message(cont, user):
	if(cont=='0'):
		return(user+" has yet to make a contribution on Github today. ")
	elif(cont=="1"):
		return("So far today, "+user+" has made "+cont+" contribution on Github. ")
	else:
		return("So far today, "+user+" has made "+cont+" contributions on Github. ")

#Returns the current contribution streak of a user
def get_streak(user):
	response = requests.get(("https://github.com/"+user))
	soup = BeautifulSoup(response.text, 'lxml')
	soup=soup.find_all('rect')
	if(soup==[]):
		return ("")
	streak=0;
	curr_day=time.strftime("%Y-%m-%d")
	print(curr_day)
	#Starting the day prior, count the number of days in a row the contribution value is !0, add 1 if they have also contributed today
	for link in range(len(soup)-1, -1,-1):
		if(soup[link].get('data-date')==curr_day):
			if(soup[link].get('data-count'!="0")):
				print("Made a contribution today")
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



def get_help(): #Returns the help text
	response="Welcome to the github contributions viewer, start your text with the username of the github user you would like to inspect."
	response+=" The second word in your text can be any of the following:"
	response+=" 'today'(returns the number of contributions the user has made today),"
	response+=" 'streak'(indicates the current contribution streak of the user)."
	response+=" 'total'(indicates the user's total number of contribution in the past year)."
	response+="\n\n Example: simonkrol streak"
	return response

def get_error(command):#Returns the text when an error has occured or an invalid command is entered
	response=command +" is not a valid command, please send the word 'about' for information on how to use the github contributions viewer."
	return response

def send_sms(message, number): #Sends a text message with the desired content to the given number
	client = TwilioRestClient(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])
	client.messages.create(from_=os.environ['TWILIO_NUMBER'],
						   to=number,
						   body=message)