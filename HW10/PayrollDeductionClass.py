class PayrollDeduction:
    
    def __init__(self, description, date, amnt, empID):
        self.__description= description
        self.__date= date
        self.__amnt= amnt
        self.__empID= empID
        
    def getDescription(self):
        return self.__description
    
    def getDate(self):
        return self.__date
    
    def getAmount(self):
        return self.__amnt
    
    def getEmployeeID(self):
        return self.__empID