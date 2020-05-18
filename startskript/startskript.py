import subprocess


def start():
    print("Programme werden gestartet.")
    subprocess.Popen("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
    subprocess.Popen("C:\\Program Files\\KeePassXC\\KeePassXC.exe")
    subprocess.Popen("C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE")
    subprocess.Popen("G:\\ARNOtop\\Programm\\Selekt.exe")


def reset():
    print("Sollen die Standardprogramme gestartet werden? (Y / N)")
    return input()


def logic(choice):
    if choice == "Y" or choice == "y":
        start()
        exit(0)
    elif choice == "N" or choice == "n":
        exit(1)
    else:
        print(choice + " ist eine ungültige Auswahl, nur Y und N sind erlaubt. \n")


while True:
    logic(reset())
