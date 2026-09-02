employees = {
    101: "Dipendra",
    102: "Rahul",
    103: "Amit"
}

print(employees.get(102))
print(employees.get(999))
print(employees.get(999, "Employee not found"))