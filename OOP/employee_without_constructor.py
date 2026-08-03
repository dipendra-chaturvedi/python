class Employee:

    def display(self):
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)

emp = Employee()
emp.emp_id = 100
emp.name = "Dipendra"
emp.salary = 60000
emp.display()

emp1 = Employee()
emp1.emp_id = 101
emp1.name = "Andrul"
emp1.salary = 60000
emp1.display()

emp2 = Employee()
emp2.emp_id = 102
emp2.name = "Rahul"
emp2.salary = 50000
emp2.display()

# Without a constructor it will repeat the same code for every object. So, we can use a constructor to avoid this repetition.