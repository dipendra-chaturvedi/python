class Employee:

    def work(self):
        print("Employee is working")

class Manager(Employee):

    def manage(self):
        print("Manager is managing")

manager = Manager()

manager.work()
manager.manage()