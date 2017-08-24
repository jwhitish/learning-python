#a simple pomodoro timer

import webbrowser
import time

print("Welcome to Py-Modoro, the simple pomodoro timer! \n")
time.sleep(2)

print("To get things started I will ask you how many sessions you would \n \
like to work for. \n \
Next I will ask you how long (in seconds) the work session should be. \n \
Last I will ask you to enter the URL of the website to send you to on break.")
time.sleep(3)

print( )
print("To get things started...")

count = int(input("How many sessions would you like? "))
duration = int(input("How long should they be? (In Seconds) "))
breakTime = str(input("Enter the full URL of your preferred break website: "))
ready = input("Ready to begin? (y/n + enter) ")

if ready == "y":
  print("Get to work!")  
  while count > 0:
    time.sleep(duration)
    webbrowser.open(breakTime)
    count -= 1
else:
    print("Ok, Another time then. Slacker...")
