# OOA
# Na farmie żyją krowy i świnie. Milkman kupuje mleko, które
# daje nam krowa ...
#
# Klasy projektowe:
# farma, krowa, świnia, mleko, milkman
#
# krowa -> żyje, daje mleko
# milkman -> kupuje
#
# OOD
# Animal:
#     name
#
#
# Cow:
#     + live
#     + get_milk -> Milk
#
# Milk:
#
# OOP

class Barn:
    pass

class Animal:
    def __init__(self, name):
        self.name = name

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.has_milk = True
        self.amount_milk = Milk(3)

    def get_milk(self):
        if self.has_milk:
            self.has_milk = False
            m = self.amount_milk
            self.amount_milk = Milk(0)
            return m

        else:
            print("Nie mam mleka")

    def eat(self):
        print("Jem")
        self.has_milk = True


class Pig(Animal):
    def __init__(self, name):
        super().__init__(name)

class Milk:
    def __init__(self, amount):
        self.amount = amount

    def sell(self, milkman):
        milkman.money -= self.amount * 10
        milkman.milk += self.amount

    def __str__(self):
        return f"Mleko, ilość: {self.amount}"

class Milkman:
    def __init__(self):
        self.milk = 0
        self.money = 100

    def buy(self, milk):
        self.milk += milk.amount
        self.money -= 10*milk.amount

mm = Milkman()
c = Cow("Mućka")

print("Przed zakupem")
print(mm.money)
print(mm.milk)
mm.buy(c.get_milk())
print("Po zakupie")
print(mm.money)
print(mm.milk)
