class Employee:
    def __init__(self, firstName, lastName, employeeId, hourlyPay):
        self.firstName = firstName
        self.lastName = lastName
        self.employeeId = employeeId
        self.hourlyPay = hourlyPay
    
    def pay(self, hoursWorked):
        if hoursWorked <= 40:
            totalPay = hoursWorked * self.hourlyPay
        else:
            overtimeHours = hoursWorked - 40
            regularPay = 40 * self.hourlyPay
            overtimePay = overtimeHours * (self.hourlyPay * 1.5)
            totalPay = regularPay + overtimePay
        return totalPay

# Propmt and math
employeeId = int(input("Please enter the Employee's ID: "))
firstName = input("Please enter the Employee's First Name: ")
lastName = input("Please enter the Employee's LastName Name: ")
hourlyPay = float(input("Please enter the Employee's Hourly Pay Rate: "))
employee = Employee(firstName, lastName, employeeId, hourlyPay)
prompt = f"How many hours did {employee.firstName} work this week? "
hoursWorked = float(input(prompt))
payAmount = employee.pay(hoursWorked)

print(f"{employee.firstName} {employee.lastName}'s paycheck amount is ${payAmount:.2f}.")
