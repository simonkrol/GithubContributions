# Github Contribution Reminder

A python script that sends you an SMS message with the number of contributions you've made that day
Makes use of a server (hosted on Heroku) that when sent a sms, can respond with a Github user's daily and yearly contribution number, as well as their current contribution streak.

### Technology
- Python 3
- Requests
- Twilio
- BeautifulSoup4
Includes a scheduler to allow you to set a specific time to run each day
Uses a heroku server to respond to text requests

### Options
- Choose which user to inspect
- Select the time to send sms or send immediately
- Send sms to retrieve information about streaks, daily contributions and yearly contributions
>Version 1.2

### Setup (Windows)
- Download or clone the repository
- Make sure `pip` and Python 3 are installed
- Install the required modules
```
$ pip install requests
$ pip install BeautifulSoup4
$ pip install schedule
```
- Create an environ.py file in the same directiory as contributions.pyw
- Create a Twilio account and generate a number to send from
- Use your Twilio account to set each of the environment variables in a method called set_env within the config.py file
```
def set_env():
	os.environ['TWILIO_ACCOUNT_SID']=...
	os.environ['TWILIO_AUTH_TOKEN']=...
	os.environ['TWILIO_NUMBER']=...#Check twilio for formatting requirements
	os.environ['MY_NUMBER']=...
```
- Set the scheduled time and your github username

### Usage
- Execute through command line
```
$ python contributions.pyw
```
- or Right click on file and run using Python