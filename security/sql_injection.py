# username = input("Enter username: ")

# unsafe_query = f"""
# SELECT * FROM users
# WHERE username = '{username}'
# """

# print(unsafe_query)


username = input("Enter username: ")

query = """
SELECT * FROM users
WHERE username = %s
"""

values = (username,)

print(query)
print(values)