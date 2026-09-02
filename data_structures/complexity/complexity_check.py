# O(1)
employee = ["Rahul", 75000]
print(employee[0])


# O(n)
employees = ["Rahul", "Amit", "Priya", "Neha"]

for employee in employees:
    print(employee)


# O(log n)
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

target = 70
left = 0
right = len(numbers) - 1

while left <= right:
    middle = (left + right) // 2

    if numbers[middle] == target:
        print("Found")
        break
    elif numbers[middle] < target:
        left = middle + 1
    else:
        right = middle - 1


# O(n²)
for employee1 in employees:
    for employee2 in employees:
        print(employee1, employee2)