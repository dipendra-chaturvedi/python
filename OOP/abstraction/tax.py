from abc import ABC, abstractmethod


class TaxCalculator(ABC):

    @abstractmethod
    def calculate_tax(self, salary):
        pass

class IndiaTax(TaxCalculator):

    def calculate_tax(self, salary):
        if salary <= 500000:
            return 0
        elif salary <= 1000000:
            return salary * 0.10
        else:
            return salary * 0.20

class USATax(TaxCalculator):

    def calculate_tax(self, salary):
        if salary <= 50000:
            return salary * 0.08
        else:
            return salary * 0.15

india = IndiaTax()
usa = USATax()

india_tax = india.calculate_tax(1200000)
usa_tax = usa.calculate_tax(1200000)

print(india_tax)
print(usa_tax)