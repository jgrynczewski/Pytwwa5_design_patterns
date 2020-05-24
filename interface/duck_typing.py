# If it looks like duck, swim like duck and quacks like
# duck, then it probably is a duck.

class Duck:
    def swim_and_quack(self):
        print("Jestem kaczką, umiem pływać i kwakać")

class Dog:
    def swim_and_quack(self):
        print("Jestem psem, umiem pływać i kwakać")

class Fish:
    def swim(self):
        print("Jestem rybą, umiem pływać, nie umiem kwakać")

def duck_test(animal):
    animal.swim_and_quack()

duck_test(Duck())
duck_test(Dog())
duck_test(Fish())