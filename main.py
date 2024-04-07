# Objective:
# build an alarm that tells the time and alarm me when it is 9pm


from datetime import datetime
import pyttsx3

engine = pyttsx3.init()

print('Welcome to a virtual alarm clock.')

try:
    am_or_pm = input("Is the time in am or pm: ").lower()
    if am_or_pm == "am":
         time_hour_indicate = int(input("Hour: "))
         time_minute_indicate = int(input("Minute: "))
    if am_or_pm == "pm":
        time_hour_indicate = int(input("Hour: ")) + 12
        time_minute_indicate = int(input("Minute: "))
except NameError:
    print("Something went wrong. \n"
          "Start again.")

try:

    cont = True

    while cont:

        now = datetime.now()

        present_hour = now.hour
        present_minute = now.minute

        if present_hour < time_hour_indicate:
            pass
        elif present_hour >= time_hour_indicate and present_minute > time_minute_indicate:
            pass
        elif present_hour == time_hour_indicate and present_minute == time_minute_indicate:
            if time_minute_indicate < 10:
                print(f"The time is {time_hour_indicate}:0{time_minute_indicate}{am_or_pm}")
                for s in range(10):
                    engine.say(f"The time is {time_hour_indicate}:0{time_minute_indicate}{am_or_pm}")
                    engine.runAndWait()
            else:
                print(f"The time is {time_hour_indicate}:{time_minute_indicate}{am_or_pm}")
                for s in range(10):
                    engine.say(f"The time is {time_hour_indicate}:{time_minute_indicate}{am_or_pm}")
                    engine.runAndWait()

            cont = False
except KeyboardInterrupt and NameError:
    print("Something went wrong.")
    print("Quitting.....")
