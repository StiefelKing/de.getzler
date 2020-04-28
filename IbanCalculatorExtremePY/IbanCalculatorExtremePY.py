import sys
import os

class Kto:
    seed = 0
    checksum = 0
    value = 0
    def __init__(self, seed,):
        self.seed = seed
        if seed > 999999999 or seed < 1:
            raise ValueError
        else:
            # initialize
            array = [int(x) for x in str(seed).zfill(9)]
            checksum = 0
            # special case
            j = 0
            if array [2] == 9:
                j = 7
            else:
                j = 6
            # calculate
            m = 2
            sum = 0
            for x in range(j):
                array[8-x] = array[8-x] * m
                m += 1
                sum = sum + array[8-x]

            # final
            checksum = 11 - sum % 11
            if sum % 11 == 1 or sum % 11 == 0:
                checksum = 0
            self.checksum = checksum
            self.value = (str(seed).zfill(9) + str(checksum))

class IBAN:
    kto = 0
    value = ""
    def __init__(self, kto, blz):
        country = 131400
        countryStr = "DE"
        self.kto = kto
        cc = 98 - (((blz*10000000000000000) + (int(kto.value)*1000000) + country) % 97)
        self.value = "DE" + str(cc).zfill(2) + " " + str(blz).zfill(8)[0:4] + " " + str(blz).zfill(8)[4:8] + " " + str(kto.value).zfill(10)[0:4] + " " + str(kto.value).zfill(10)[4:8] + " " + str(kto.value).zfill(10)[8:10]
while 1:
    try:
        print("IBAN ausgeben von: ")
        start = int(input())
        print("IBAN ausgeben bis:  ")
        end = int(input())
    except:
        sys.exit(0)
    if os.path.exists("List.txt"):
        os.remove("List.txt")
    f = open("List.txt","a")
    f.write("IBAN List for 73369920 von " + str(start) + " bis " + str(end) + "\n")
    for i in range(start, end+1):
        iban = IBAN(Kto(i), 73369920)
        out = iban.kto.value + " | " + iban.value
        print(out)
        f.write(out + "\n")
    f.close()