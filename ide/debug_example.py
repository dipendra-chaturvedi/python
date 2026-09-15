def calculate_salary(salary, bonus):
    total = salary + bonus
    return total


salary = 60000
bonus = 10000

total_salary = calculate_salary(salary, bonus)

print("Total Salary:", total_salary)