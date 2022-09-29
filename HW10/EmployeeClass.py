class Employee:

    def __init__(self, name, ID, department, job_title, salary):
        self.__name= name
        self.__ID= ID
        self.__department= department
        self.__job_title= job_title
        self.__salary= salary
    
    def getName(self):
        return self.__name
    
    def getID(self):
        return self.__ID
    
    def getDepartment(self):
        return self.__department
    
    def getJobTitle(self):
        return self.__job_title
    
    def getSalary(self):
        return self.__salary