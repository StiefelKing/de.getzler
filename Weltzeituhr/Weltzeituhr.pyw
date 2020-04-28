from tkinter import *
from datetime import *
import pytz

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
b1 = []     # toggle Alarm
b2 = []     # snooze Alarm

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
    l6.append(Label(frame[x], text = "HH-MM"))
    l6[x].pack(side = TOP, fill = "x")
    b1.append(Button(frame[x], text = "Alarm toggle"))
    b1[x].pack(side = TOP, fill = "x")
    b2.append(Button(frame[x], text = "Snooze", state=DISABLED))
    b2[x].pack(side = TOP, fill = "x")
root. geometry("400x180")

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
    root.update_idletasks()
    root.update()