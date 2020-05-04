import pytz
import winsound
from time import sleep
from datetime import *
from tkinter import *


def set_alarm(x_local):
    pattern = re.compile("^([0-9]{2}):([0-9]{2})$")
    if pattern.match(e1[x_local].get()):
        if not f1[x_local]:
            l6[x_local].config(text=e1[x_local].get())
            f1[x_local] = True
        else:
            l6[x_local].config(text="HH:MM")
            b2[x_local].config(state=DISABLED)
            f1[x_local] = False
            f2[x_local] = False


def snooze(x_local):
    if f2[x_local]:
        alarm_text = l6[x_local].cget("text").split(":")
        alarm_text[0] = int(alarm_text[0])
        alarm_text[1] = int(alarm_text[1])
        alarm_text[1] += 5
        if alarm_text[1] >= 60:
            alarm_text[1] -= 60
            alarm_text[0] += 1
            if alarm_text[0] >= 24:
                alarm_text[0] -= 24
        l6[x_local].config(text=str(alarm_text[0]).zfill(2) + ":" + str(alarm_text[1]).zfill(2))
        f2[x_local] = False
        b2[x_local].config(state=DISABLED)


def compare_alarm(time_local, x_local):
    if time_local == l6[x_local].cget("text") and f1[x_local]:
        b2[x_local].config(state=NORMAL)
        f2[x_local] = True


def alarm(x_local):
    sleep(0.05)
    winsound.Beep(1000, 100)


# initialize GUI
# Declarations
root = Tk()  # root plane
root.title("Weltzeituhr")
frame = []  # frames for clocks
l1 = []  # label "Timezone"
l2 = []  # label "Uhrzeit"
l3 = []  # label Time
l4 = []  # label Date
l5 = []  # label "Alarm"
l6 = []  # label alarm_time
e1 = []  # Entrybox
b1 = []  # toggle Alarm
b2 = []  # snooze Alarm
f1 = [False] * 3  # Flag, if Alarm is set
f2 = [False] * 3  # Flag, if Alarm is ringing
# Assignment
for x in range(3):
    frame.append(Frame(root))
    frame[x].pack(fill="both", side=LEFT, expand=True)
    l1.append(Label(frame[x], text="UTF +X"))
    l1[x].pack(side=TOP, fill="x")
    l2.append(Label(frame[x], text="Uhrzeit:"))
    l2[x].pack(side=TOP, fill="x")
    l3.append(Label(frame[x], text="HH-MM-SS"))
    l3[x].pack(side=TOP, fill="x")
    l4.append(Label(frame[x], text="YYYY-MM-DD"))
    l4[x].pack(side=TOP, fill="x")
    l5.append(Label(frame[x], text="Alarm:"))
    l5[x].pack(side=TOP, fill="x")
    l6.append(Label(frame[x], text="HH:MM"))
    l6[x].pack(side=TOP, fill="x")
    e1.append(Entry(frame[x], justify="center"))
    e1[x].insert(10, "HH:MM")
    e1[x].pack(side=TOP, fill="x")
    b1.append(Button(frame[x], text="Alarm toggle"))
    b1[x].pack(side=TOP, fill="x")
    b2.append(Button(frame[x], text="Snooze", state=DISABLED))
    b2[x].pack(side=TOP, fill="x")
b1[0].config(command=lambda: set_alarm(0))
b1[1].config(command=lambda: set_alarm(1))
b1[2].config(command=lambda: set_alarm(2))
b2[0].config(command=lambda: snooze(0))
b2[1].config(command=lambda: snooze(1))
b2[2].config(command=lambda: snooze(2))
root.geometry("400x200")

# clock functionality
tz = {
    0: pytz.timezone("Europe/Berlin"),
    1: pytz.timezone("UTC"),
    2: pytz.timezone("America/New_York")
}

# loop for GUI
while True:
    for x in range(3):
        clock = datetime.now(tz.get(x, timezone.utc)).strftime("%H:%M:%S")
        date = datetime.now(tz.get(x, timezone.utc)).strftime("%d.%m.%Y")
        zone = datetime.now(tz.get(x, timezone.utc)).strftime("%Z %z")
        l1[x].config(text=zone)
        l3[x].config(text=clock)
        l4[x].config(text=date)
        compare_alarm(datetime.now(tz.get(x, timezone.utc)).strftime("%H:%M"), x)
        if f2[x]:
            alarm(x)
            l5[x].config(bg="red")
        else:
            l5[x].config(bg="SystemButtonFace")
    root.update_idletasks()
    root.update()
    sleep(0.25)
