from abc import *
class RBI(ABC):
    def min_bal(self):
        pass
    def RI(self):
        print("RI is 6.5%")
class SBI(RBI):
    def min_bal(self):
        print("Min balance is 2000 rupees !")
class HDFC(RBI):
    def min_bal(self):
        print("Min balance is 0 rupees !")
class ICICI(RBI):
    def min_bal(self):
        print("Min balance is 1000 rupees !")
s=SBI()
s.min_bal()
s.RI()
h=HDFC()
h.min_bal()
h.RI()
i=ICICI()
i.min_bal()
i.RI()