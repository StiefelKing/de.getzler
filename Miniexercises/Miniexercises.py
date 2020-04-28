from array import *
from random import *
from math import *

def fibonacci():
    print("")
    print("Bis zu welchem Element soll die Sequenz berechnet werden?")
    print("-1 = bis Element -1")
    print(" 0 = bis Element  0")
    print(" 1 = bis Element  1")
    endNumber = int(input())
    fibonacciNumbers = [None] * (abs(endNumber)+1)
    if endNumber < -1:
        fibonacciNumbers[0] = 0
        fibonacciNumbers[1] = 1
        i = 2
        while i < abs(endNumber)+1:
            fibonacciNumbers[i] = fibonacciNumbers[i-2] - fibonacciNumbers[i-1]
            i += 1
    elif endNumber == -1:
        fibonacciNumbers[0] = 0
        fibonacciNumbers[1] = 1
    elif endNumber == 0:
        fibonacciNumbers[0] = 0
    elif endNumber == 1:
        fibonacciNumbers[0] = 0
        fibonacciNumbers[1] = 1
    elif endNumber > 1:
        fibonacciNumbers[0] = 0
        fibonacciNumbers[1] = 1
        i = 2
        while i < endNumber+1:
            fibonacciNumbers[i] = fibonacciNumbers[i-2] + fibonacciNumbers[i-1]
            i += 1
    print(fibonacciNumbers)

def faculty():
    print("")
    print("Welche Fakultät soll berechnet werden?")
    try:
        faculty = int(input())
        if faculty < 0:
            output = "undefined"
        elif faculty == 0:
            output = 1
        else:
            output = 1
            while faculty > 0:
                output = faculty * output
                faculty = faculty - 1
    except:
        print("invalid Input")
    print(output)

def minimum():
    my_array = [4, 7, 87, 12, -56, 9, -8, 4, -2, 5, 78 , 90, -4, 2, 5, 0, 42]
    my_array.sort()
    print("")
    print("Das niedrigste Element ist:", my_array[0])

def maximum():
    my_array = [4, 7, 87, 12, -56, 9, -8, 4, -2, 5, 78 , 90, -4, 2, 5, 0, 42]
    my_array.sort(reverse=True)
    print("")
    print("Das höchste Element ist:", my_array[0])

def sumArray():
    my_array = [4, 7, 87, 12, -56, 9, -8, 4, -2, 5, 78 , 90, -4, 2, 5, 0, 42]
    print("")
    print("Sie Summe ist:", sum(my_array))

def average():
    my_array = [4, 7, 87, 12, -56, 9, -8, 4, -2, 5, 78 , 90, -4, 2, 5, 0, 42]
    print("")
    print("Der Mittelwert ist:", sum(my_array)/len(my_array))

def inversPyramid():
    print("")
    print("Wie hoch soll die Pyramide sein?")
    number = int(input())
    print("")
    while number > 0:
        print("*" * number)
        number -= 1

def pyramid():
    print("")
    print("Wie hoch soll die Pyramide sein?")
    number = int(input())
    i = 1
    print("")
    while i <= number:
        print("*" * i)
        i += 1

def exponent():
    print("")
    print("Welche Basis?")
    base= int(input())
    print("")
    print("Welcher Exponent?")
    exponent = int(input())
    print("")
    print("Das Ergebnis lautet: ", base**exponent)

def multiply(number, multiples):
    array = [None] * multiples
    i = 2
    array[0] = number
    while i <= multiples:
        array[i-1] = array[0] * i
        i += 1
    return array

def small1x1():
    print("")
    print("Welche Zahl?")
    number = int(input())
    print(multiply(number, 10))

def multiples():
    print("")
    print("Welche Zahl?")
    number = int(input())
    print("")
    print("Wie viele Vielfache?")
    multiples = int(input())
    print(multiply(number, multiples))

def monteCarloThrow():
    #array (0 = x, 1 = y, 2 = boolCircle, 3 = boolSquare)
    array = [0,0,0,0]
    array[0] = random()
    array[1] = random()
    line = sqrt(array[0]**2+array[1]**2)
    if line <= 1:
        array[2] = 1
        array[3] = 1
    else:
        array[2] = 0
        array[3] = 1
    return array

def monteCarlo():
    print("")
    print("Wie viele Versuche?")
    number = int(input())
    inSquare = 0
    inCircle = 0
    while number > 0:
        arr = monteCarloThrow()
        inCircle += arr[2]
        inSquare += arr[3]
        number -=1
    print("Ergebnis für π: ",inCircle/inSquare*4)

def switch1(functionChoice):
    switcher = { 
        1: fibonacci,
        2: faculty,
        3: minimum,
        4: maximum,
        5: sumArray,
        6: average,
        7: inversPyramid,
        8: pyramid,
        9: exponent,
        10: small1x1,
        11: multiples,
        12: monteCarlo,
    }
    func = switcher.get(functionChoice, lambda: "falsche Eingabe")
    func()

while 1:
    print("")
    print("Welche Funktion soll ausführt werden?")
    print(" 1 Fibonacci")
    print(" 2 Fakultät")
    print(" 3 Minimum")
    print(" 4 Maximum")
    print(" 5 Summe")
    print(" 6 Mittelwert")
    print(" 7 Umgekehrte Pyramide")
    print(" 8 Pyramide")
    print(" 9 Exponent")
    print("10 kleines 1x1")
    print("11 Vielfache")
    print("12 Monte Carlo")
    print("")
    try:
        switch1(int(input()))
    except:
        print("invalid Input")