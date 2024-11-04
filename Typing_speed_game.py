#importing modules which are required in this program
from time import *
import random as r

#function for counting mistakes: using try-except to avoid crashing the game
def mistakes(para_test, user_test):
    error = 0
    for x in range (len(para_test)):
        try:
            if para_test[x] != user_test[x]:
                error = error + 1
        except:
            error = error + 1
    return error

#funtion for calculating time and speed (time_s = starting time, time_e = ending time, time_R is round-off) 
def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    speed = len(userinput) / time_R
    return round(speed)


#below are few paragraphs of strings for typing test within a list, of course you can easily  cheat with copy paste, but come on dont be like that!

test = ["A paragraph is a self-contained unit of discourse in writing, dealing with a particular point or idea.",
 "i will never give up, even if i had to take as many breaks as possible to reach my goal!",
 "I should never cheat by copy-pasting stuff in a typing test like this one!. because if i did, i would be the world's biggest stupid person." ]

#using choice module (from random) so we can have a randomly generated string from the list for the user

test1 = r.choice(test)

#greetings

print("--------->Welcome to The typing speed test game!<---------\n")

#taking permission to start

user_consent = (input('''type "start" to begin the game:   '''))
user_consent = user_consent.lower()

#start:
if "start" in user_consent:
    print (test1)
else:
    print("you didnt type start. bye")

# line breaks below
print()
print()
#line breaks above

#using time functions to set a timer

time_1 = time()

test_input = input("Go!!:  ")

time_2 = time()

#calculating final results:

print("Speed: ", speed_time(time_1, time_2, test_input), "w/sec")
print("Errors: ", mistakes(test1, test_input))

print("Thanks a lot for playing!, developed by The_coding_lynx ")




