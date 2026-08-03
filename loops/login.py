correct_password = "python"

while True:

    password = input("Enter Password : ")

    if password == correct_password:
        print("Login Successful")
        break

    print("Wrong Password")