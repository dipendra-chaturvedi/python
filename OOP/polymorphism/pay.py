class Payment:

    def pay(self):
        print("Payment Done")


class CreditCard(Payment):

    def pay(self):
        print("Paid using Credit Card")


class UPI(Payment):

    def pay(self):
        print("Paid using UPI")


CreditCard().pay()
UPI().pay()