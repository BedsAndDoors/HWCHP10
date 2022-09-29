from EmployeeClass import Employee
from PayrollDeductionClass import PD

emp= Employee('Jimmy Smith',58475,'Information Systems','Developer',6800)

ded1= PD('food court','8/14/2022',22.50,39119)
ded2= PD('gift contribution','8/12/2022',25.00,58475)
ded3= PD('food court','8/17/2022',15.25,21547)
ded4= PD('vending machine','8/22/2022',3.00,58475)
ded5= PD('vending machine','8/5/2022',2.75,58475)

print("*** Employee Pay ***")
print("Name:       ", emp.getName())
print("ID Number:  ", emp.getID())
print("Department: ", emp.getDepartment())
print("Gross Pay:   $", float(emp.getSalary()), sep='')
print("Net Pay:     $", emp.getSalary()-ded2.getAmount()-ded4.getAmount()-ded5.getAmount(), sep='')

