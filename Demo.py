##public
##protected_
##private__

class Bank:
    def __init__(self,custName,custID,balance):
        self.__custName=custName
        self.__custID=custID
        self.__Balance=balance
    def getCustName(self):
        return self.__custName
    def getCustID(self):
        return self.__custID
    def getBalance(self):
        return self.__Balance
    def setCustName(self,custName):
        self.__custName=custName
    def setCustID(self,custID):
        self.__custID=custID
    def setBalance(self,balance):
        self.__Balance=balance

b=Bank("abi","34232",1000)
print(b.getCustName())
b.setCustName("arul")
print(b.getCustName())
