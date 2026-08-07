from collections import Counter

departments = [
    "Developer",
    "Tester",
    "Developer",
    "HR",
    "Tester",
    "Developer",
    "Manager"
]

department_count = Counter(departments)

print(department_count)

#Counter()        # Count frequency
#defaultdict()    # Dictionary with default values
#deque()          # Fast queue/stack
#OrderedDict()    # Ordered dictionary (legacy use)
#namedtuple()     # Lightweight class/object