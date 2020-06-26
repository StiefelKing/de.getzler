from datetime import datetime
from subprocess import Popen
from time import sleep
import schedule
from pynput.keyboard import Key, Controller


def compare_time(input_time):
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    if input_time == current_time:
        return True
    else:
        return False


def validate(input_time):
    try:
        return datetime.strptime(input_time, "%H:%M")
    except ValueError:
        print(ValueError)
        exit(-1)


def action():
    print("Anmeldung erfolgt.")
    Popen(["C:\\Program Files (x86)\\Time-Organizer\\Time-Organizer.exe", "//einmal"])
    sleep(5)
    keyboard = Controller()
    keyboard.type("Kätzlmeier")
    sleep(1)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    sleep(1)
    keyboard.type("XXX")
    sleep(1)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    sleep(1)
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    exit()


login_time = input("Zeit im Format HH:MM eingeben: ")
input_time_main = validate(login_time)
schedule.every().day.at(input_time_main.strftime("%H:%M")).do(action)
while True:
    schedule.run_pending()
    sleep(1)
