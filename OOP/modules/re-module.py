import re

email = input("Enter Employee Email: ")

pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")

#re.match()      # Match from beginning
#re.search()     # Find first match
#re.findall()    # Find all matches
#re.finditer()   # Iterator of matches
#re.sub()        # Replace text
#re.split()      # Split using pattern
#re.compile()    # Compile regex