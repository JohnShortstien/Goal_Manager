#!/usr/bin/env python3

from datetime import datetime

is_end_date = False

user_fix_text = "The amount of benchmarks or the time for each benchmark will not result in you completing by the expected date. Your options are:\n \
[1] Change date of completing goal so all benchmarks fit into the desired time.\n \
[2] Change the amount of time used by each benchmark.\n \
[3] Change the amount of benchmarks to complete the goal.\n"

def bol_userInput(text):
    userInput = input(text)
    if "y" in userInput:
        return True
    elif "n" in userInput:
        return False
    else:
        print("There was an error. Try again.")
        bol_userInput(text)

def benchmark_goals():
    if bol_userInput("Do you want all benchmarks to be the same amount of time?\n"):
        benchmark_time = int(input("How many days do you want benchmarks to last?\n"))
        if is_end_date:
            if (number_of_benchmarks * benchmark_time) > days_to_completion:
                user_fix_choose = input(user_fix_text)

            elif (number_of_benchmarks * benchmark_time) < days_to_completion:
                if bol_userInput("The amount of time it takes for all of your benchmarks to be\
finished does not corrispond with the day of completion. Would you like to change it so it does?\n"):
                    user_fix_choose = input(user_fix_text)
        add_benchmark_time = False

    else:
        add_benchmark_time = True


    for x in range(number_of_benchmarks):
        benchmarks = input("What should benchmark #"+str(x+1)+" be?\n")
        daily_task = input("What can you do every day to work towards benchmark #"+str(x+1)+"\n")
        if add_benchmark_time:
            benchmark_time = int(input("How many days do you want this benchmark to last?\n"))
        else:
            print("Your benchmark time is " + str(benchmark_time)+"days.\n")

todays_date = datetime.now()

goal = input("What is your goal?\n")

if bol_userInput("Do you want to set a deadline?\n"):
    completion_day = datetime.strptime(input("When do you want to complete it by?\n"), "%m/%d/%Y")
    is_end_date = True

    time_elasped = completion_day - todays_date
    days_to_completion = time_elasped.days
    number_of_benchmarks = int(days_to_completion/7)

    if bol_userInput("Your goal splits into "+str(number_of_benchmarks)+" benchmarks for 1 benchmark each week. Do you want to change it?\n"):
        number_of_benchmarks = int(input("How many benchmarks do you want?\n"))
        print("Okay you will have "+str(number_of_benchmarks)+" benchmarks.\n")

    else:
        print("Okay you will have "+str(number_of_benchmarks)+" benchmarks.\n")

else:
    is_end_date = False

if is_end_date:
     benchmark_goals()

elif not is_end_date:
    number_of_benchmarks = int(input("How many benchmarks do you want?\n"))
    benchmark_goals()
