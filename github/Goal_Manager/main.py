#!/usr/bin/env python3

from datetime import datetime

todays_date = datetime.now()

goal = input("What is your goal?")

completion_day = datetime.strptime(input("When do you want to complete it by?"), "%m/%d/%Y")

#Store variables goal and completion_day in file

days_to_completion = completion_day - todays_date
