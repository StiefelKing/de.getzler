from tkinter import *
from datetime import *
import pytz

def setAlarm(x):
    if e1[x].get() != "HH:MM":
        if b3[x] == False:
            l6[x].config(text=e1[x].get())
            b2[x].config(state=NORMAL)
            b3[x] = True
        else:
            l6[x].config(text="HH:MM")
            b2[x].config(state=DISABLED)
            b3[x] = False

def compareAlarm(x):
    print("under construction") # compare strings

def alarm(x):
    print("Alarm"+str(x)) # send Alarms

# initialize GUI
root = Tk() # root plane
root.title("Weltzeituhr")
frame = []  # frames for clocks
l1 = []     # label "Timezone"
l2 = []     # label "Uhrzeit"
l3 = []     # label Time
l4 = []     # label Date
l5 = []     # label "Alarm"
l6 = []     # label Alarmtime
e1 = []     # Entrybox
b1 = []     # toggle Alarm
b2 = []     # snooze Alarm
b3 = [False]*3     # Flag, if Alarm is set

for x in range(3):
    frame.append(Frame(root))
    frame[x].pack(fill="both", side = LEFT, expand = True)
    l1.append(Label(frame[x], text = "UTF +X"))
    l1[x].pack(side = TOP, fill = "x")
    l2.append(Label(frame[x], text = "Uhrzeit:"))
    l2[x].pack(side = TOP, fill = "x")
    l3.append(Label(frame[x], text = "HH-MM-SS"))
    l3[x].pack(side = TOP, fill = "x")
    l4.append(Label(frame[x], text = "YYYY-MM-DD"))
    l4[x].pack(side = TOP, fill = "x")
    l5.append(Label(frame[x], text = "Alarm:"))
    l5[x].pack(side = TOP, fill = "x")
    l6.append(Label(frame[x], text = "HH:MM"))
    l6[x].pack(side = TOP, fill = "x")
    e1.append(Entry(frame[x], justify="center"))
    e1[x].insert(10, "HH:MM")
    e1[x].pack(side = TOP, fill = "x")
    b1.append(Button(frame[x], text = "Alarm toggle"))
    b1[x].pack(side = TOP, fill = "x")
    b2.append(Button(frame[x], text = "Snooze", state=DISABLED))
    b2[x].pack(side = TOP, fill = "x")
b1[0].config(command = lambda: setAlarm(0))
b1[1].config(command = lambda: setAlarm(1))
b1[2].config(command = lambda: setAlarm(2))
root. geometry("400x200")

# clock functionality
tz = { 
    0: pytz.timezone("Europe/Berlin"),
    1: pytz.timezone("UTC"),
    2: pytz.timezone("America/New_York")
    }
while True:
    for x in range(3):
        clock = datetime.now(tz.get(x, timezone.utc)).strftime("%H:%M:%S")
        date = datetime.now(tz.get(x, timezone.utc)).strftime("%d.%m.%Y")
        zone = datetime.now(tz.get(x, timezone.utc)).strftime("%Z %z")
        l1[x].config(text=str(zone))
        l3[x].config(text=str(clock))
        l4[x].config(text=str(date))
        compareAlarm(x)
    root.update_idletasks()
    root.update()