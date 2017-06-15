
import helper
import config#File used to set environment variables
import os
import schedule
import time


username='simonkrol'
send_time="22:00"


def run():
	config.set_env()
	helper.send_sms(helper.get_contributions(username), os.environ["MY_NUMBER"])
x=helper.get_contributions("simonkrol")
print(x)
schedule.every().day.at(send_time).do(run)
while True:
	schedule.run_pending()
	time.sleep(60)