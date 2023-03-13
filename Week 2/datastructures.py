Data1 = [7, False, "Apple", True, 7, 98.6]
Data2 = ["July", 4, 8, "Tango", 4.3, "Bingo"]
Data3 = ["A", 7, -1, 3.14, True, 7]
# The data was presented incorrectly in the assignment
# Data4 = ["name" = "Joe", "age" = 26, "active" = True, "hourly_wage" = 14.75]
# This is the correct format to have it store properly
Data4 = {"name": "Joe", "age": 26, "active": True, "hourly_wage": 14.75}

# DataSet1 
print(len(Data1))
print(Data1[3])
print(Data1.count(7))

# DataSet2
import random
random_index = random.randint(0, len(Data2)-1)
removed_item = Data2.pop(random_index)
Data2.insert(random_index, "Alpha")
print(Data2)

# DataSet3
# Some editing had to be done here to meet expected code output as it needed to be stored
# in reverse and not just printed as the steps in the assignment asked
Data3 = Data3[::-1]
Data3[1] = 'B'
Data3.pop()
print(Data3)

# DataSet4
Data4["active"] = False
Data4["address"] = "123 West Main Street"
weekly_salary = Data4["hourly_wage"] * 40
print(weekly_salary)
print("name: {}, age: {}, active: {}, hourly_wage: {}, address: {}".format(
    Data4["name"], Data4["age"], Data4["active"], Data4["hourly_wage"], Data4["address"]
))