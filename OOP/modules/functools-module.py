from functools import lru_cache

@lru_cache(maxsize=100)
def calculate_bonus(employee_id):

    print(f"Calculating bonus for Employee {employee_id}...")

    basic_salary = 60000
    bonus = basic_salary * 0.20

    return bonus

print(calculate_bonus(101))
print(calculate_bonus(101))
print(calculate_bonus(101))


#lru_cache()     # Cache function results
#reduce()        # Reduce list to one value
#partial()       # Pre-fill function arguments
#wraps()         # Preserve decorator metadata