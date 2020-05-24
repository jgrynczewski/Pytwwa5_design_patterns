import abc


class TaxCalculator(abc.ABC):
    @abc.abstractmethod
    def calculate_tax(self):
        pass


class TaxCalculator2019(TaxCalculator):

    def calculate_tax(self):
        return 0

class TaxCalculator2020(TaxCalculator):

    def calculate_tax(self):
        return 2


class Main:

    @staticmethod
    def main(calc):
        tax = calc().calculate_tax()
        return tax

print(Main.main(TaxCalculator2019))
print(Main.main(TaxCalculator2020))