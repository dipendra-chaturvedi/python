class Bank:

    def __init__(self):
        self.__balance = 1000

    def show_balance(self):
        print(self.__balance)

bank = Bank()

bank.show_balance()