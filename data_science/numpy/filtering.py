import numpy as np

salaries = np.array([50000, 60000, 70000, 80000, 90000])

high_salary = salaries[salaries > 60000]

print("Salaries above 60000:", high_salary)