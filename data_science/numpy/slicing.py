import numpy as np

salaries = np.array([50000, 60000, 70000, 80000, 90000])

print("First 3:", salaries[0:3])
print("Middle:", salaries[1:4])
print("Last 2:", salaries[-2:])

# array[start : stop]
# output 
# First 3: [50000 60000 70000]
# Middle: [60000 70000 80000]
# Last 2: [80000 90000]
