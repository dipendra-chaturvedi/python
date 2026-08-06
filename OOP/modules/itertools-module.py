from itertools import combinations

employees = [
    "Dipendra",
    "Rahul",
    "Andrul",
    "Amit"
]

panels = combinations(employees, 2)

for panel in panels:
    print(panel)

#combinations()      # All unique combinations
#permutations()      # All arrangements
#product()           # Cartesian product
#chain()             # Merge iterables
#cycle()             # Infinite cycle
#count()             # Infinite counter
#repeat()            # Repeat value