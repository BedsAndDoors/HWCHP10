class Employee:

    def __init__(self, name, ID, dep, job_title, salary):
        self.__name= name
        self.__ID= ID
        self.__dep= dep
        self.__job_title= job_title
        self.__salary= salary
    
    def getName(self):
        return self.__name
    
    def getID(self):
        return self.__ID
    
    def getDepartment(self):
        return self.__dep
    
    def getJobTitle(self):
        return self.__job_title
    
    def getSalary(self):
        return self.__salary