# ENKAPSULACJA
# GETTER (ACCESSOR), SETTER (MUTATOR), DELETER
# DATA HIDING
# ACCESS MODIFIERS (_, __)
# PROPERTY


class Account:
    def __init__(self, balance):
        self.__balance = balance

    # setter (mutator)
    def set_balance(self, value):
        if type(value) != int or value < 0:
            print("Niepoprawna wartość")
        else:
            self.__balance = value

    # getter (accessory)
    def get_balance(self):
        return self.__balance

a = Account(100)
a.set_balance(250)
a.set_balance(-350)
print(a.get_balance())

# Data hiding -> access modifiers (modyfikatory dostępu)
# foo zmienna publiczna
# _foo zmienna chroniona
# __foo zmienna prywatna

a.set_balance(a.get_balance() + 2*a.get_balance()**2 )
print(a.get_balance())

# Property

class Account2:
    def __init__(self, balance):
        self.__balance = balance

    # setter (mutator)
    def set_balance(self, value):
        if type(value) != int or value < 0:
            print("Niepoprawna wartość")
        else:
            self.__balance = value

    # getter (accessory)
    def get_balance(self):
        return self.__balance

    balance = property(get_balance, set_balance)

a = Account2(100)
a.balance = -300
a.balance = 5
print(a.balance)

# Property przy użyciu dekoratorów
# syntactic sugar

class Account3:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if type(value) != int or value < 0:
            print("Niepoprawna wartość")
        else:
            self.__balance = value

a = Account3(100)
a.balance = -300
a.balance = 25
print(a.balance)