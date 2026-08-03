class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

student = Student("Dipendra")

student.display()
print(student.name)
