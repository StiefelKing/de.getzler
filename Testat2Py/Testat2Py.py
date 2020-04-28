import random

class LottoMachine:
    lottoNumbers =  0
    def __init__(self):
        self.lottoNumbers = [0] * 6

    def resetNumbers(self):
        self.lottoNumbers.clear()
        self.lottoNumbers = [0] * 6

    def makeOneNumber(self):
        flag = True
        while flag:
            num = random.randint(1,50)
            if num not in self.lottoNumbers:
                for x in range(len(self.lottoNumbers)):
                    if self.lottoNumbers[x] == 0:
                        self.lottoNumbers[x] = num
                        flag = False
                        break

    def makeNewNumbers(self):
        while 0 in self.lottoNumbers:
            self.makeOneNumber()

    def  toString(self):
        return self.lottoNumbers

myLotto = LottoMachine()
myLotto.makeNewNumbers()
print(myLotto.toString())
myLotto.resetNumbers()
myLotto.makeNewNumbers()
print(myLotto.toString())