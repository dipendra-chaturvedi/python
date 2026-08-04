# Hide data and control access.

class Bank:

    def __init__(self):
        self.__balance = 1000

bank = Bank()

print(bank.__balance)