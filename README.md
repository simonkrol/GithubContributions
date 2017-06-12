# Github Contribution Reminder

A python script that sends you an SMS message with the number of contributions you've made that day

### Technology
- Python
- Requests
- Twilio
Includes a scheduler to allow you to set a specific time to run each day

### Options
- Choose which user to inspect
- Select the time to send sms or send immediately
>Version 1.1

### Setup
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
- Use your Twilio account to set each of the environment variables in a method called set_env within the environ.py file
```
os.environ['TWILIO_ACCOUNT_SID']=...
```
- Change the scheduled time and username
- Run
```
$ python contributions.pyw
```
