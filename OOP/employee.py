# Real-Life Example
# self.variable = parameter

class Employee:

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)

emp = Employee(101, "Dipendra", 60000)
emp.display() 
emp1 = Employee(102, "Andrul", 60000)
emp1.display() 
emp2 = Employee(103, "Rahul", 50000)
emp2.display() 

# easy to create a new object with different values without repeating the same code for every object.