from abc import ABC,abstractmethod

class Bank(ABC):
    @abstractmethod
    def getROI(self):
        pass
    
    def calculateSI(self,pa,ny):
        rate = self.getROI()
        si = (rate * pa * ny)/100
        return si
    
class SBI(Bank):
    def getROI(self):
        return 7.5
    
class BOI(Bank):
    def getROI(self):
        return 10.5


boi = BOI()
print(boi.calculateSI(10000,2))

sbi = SBI()
print(sbi.calculateSI(10000,2))

# PI = 500000
# NY = 2
# ROI= 10%
