import math
import argparse

def Viruscalculator(infected, weeks, increaseRate, mortality):
    print("")
    print(" Week" + "   Infections" + "       Deaths")
    for i in range(1, weeks+1):
        dead = round(infected * mortality)
        print(str(i).rjust(5) + " " + str(infected).rjust(12) + " " + str(dead).rjust(12))
        infected = infected + round(infected * increaseRate)

parser = argparse.ArgumentParser(add_help = True)
parser.add_argument("Infizierte", type = int, help = "Die Zahl der Infizierten zu Beginn der Kalkulation.")
parser.add_argument("Wochen", type = int, help = "Die Anzahl der Wochen, die berechnet werden sollen.")
parser.add_argument("Steigerungsrate", type  =  float, help = "Die wöchentliche Steigerungsrate in % (z.B. 25.5)")
parser.add_argument("Todesrate",type = float, help = "Die wöchentliche Mortalität in % (z.B. 3.5)")
args = parser.parse_args()
print("Infizierte: {} Wochen: {} Infektionsrate: {} % Todesrate {} %".format(args.Infizierte, args.Wochen, args.Steigerungsrate, args.Todesrate))
Viruscalculator(args.Infizierte, args.Wochen, (args.Steigerungsrate / 100), (args.Todesrate / 100))