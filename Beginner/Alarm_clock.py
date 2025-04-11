import datetime
import time
from playsound import playsound

def alarm_clock(hour, min, period):
    if period== 'PM' and hour != 12:
        hour += 12
    elif period == 'AM' and hour == 12:
        hour = 0

    while True:
        now = datetime.datetime.now()
        if now.hour == hour and now.minute == min:
            print("Alarm Start")
            playsound("Cheap_Thrills.mp3")
            time.sleep(5)
            break
        time.sleep(1)

alarm_hour = int(input("Enter hour (1-12): "))
alarm_minute = int(input("Enter minutes: "))
alarm_period = input("AM or PM: ").upper()

alarm_clock(alarm_hour, alarm_minute, alarm_period)