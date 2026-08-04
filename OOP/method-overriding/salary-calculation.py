class Employee:

    def calculate_salary(self):
        return 0


class Developer(Employee):

    def calculate_salary(self):
        basic = 50000
        bonus = 10000
        return basic + bonus


class Tester(Employee):

    def calculate_salary(self):
        basic = 40000
        allowance = 5000
        return basic + allowance


dev = Developer()
tester = Tester()

print(dev.calculate_salary())
print(tester.calculate_salary())