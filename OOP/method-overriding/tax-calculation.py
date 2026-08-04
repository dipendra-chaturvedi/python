class Tax:

    def calculate_tax(self, amount):
        return amount

class IndiaTax(Tax):

    def calculate_tax(self, amount):
        return amount * 0.18

class USATax(Tax):

    def calculate_tax(self, amount):
        return amount * 0.10

india = IndiaTax()
usa = USATax()

print(india.calculate_tax(1000))
print(usa.calculate_tax(1000))