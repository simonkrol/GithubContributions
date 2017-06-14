
import helper
import environ#File used to set environment variables
import os
import schedule
import time


username='simonkrol'
send_time="22:00"


def run():
	environ.set_env()
	helper.send_sms(helper.get_response(username), os.environ["MY_NUMBER"])

schedule.every().day.at(send_time).do(run)
while True:
	schedule.run_pending()
	time.sleep(60)