#!/usr/bin/env python

import logging
import schedule
import time as tm

scheduledTime = "17:27"

logging.basicConfig(level="INFO")

def job0(schduledAt):
    logging.info("This job has been scheduled at schduledAt")

def job1():
    logging.info("Running")

# schedule.every().day.at(scheduledTime).do(job0(scheduledTime))
schedule.every(1).seconds.do(job1)

while True:
    schedule.run_pending()
    tm.sleep(1)
    