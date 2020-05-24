# OCP - Open Close Principle

from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:

    def filter_by_color(self, products, color):
        for item in products:
            if item.color == color:
                yield item

    def filter_by_size(self, products, size):
        for item in products:
            if item.size == size:
                yield item

    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.size == size and p.color==color:
                yield p


apple = Product("apple", Color.GREEN, Size.SMALL)
tree = Product("tree", Color.GREEN, Size.MEDIUM)
house = Product("house", Color.BLUE, Size.LARGE)

products = [apple, tree, house]

pf = ProductFilter()
print("Produkty zielone:")

for p in pf.filter_by_color(products, Color.GREEN):
    print(f"{p.name} jest zielony.")

print("Produkty Large")
for p in pf.filter_by_size(products, Size.LARGE):
    print(f"{p.name} jest duży.")

# Enterprise design patterns - Specification

class Specificaion:
    def is_satisfied(self, item):
        pass

class Filter():
    def filter(self, items, specification):
        pass

class ColorSpecification(Specificaion):
    def __init__(self, color):
        self.color = color

    def __and__(self,other):
        return AndSpecification(self, other)

    def is_satisfied(self, item):
        return item.color == self.color

class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


# Kod kliencki

products = [apple, tree, house]

bf = BetterFilter()
green = ColorSpecification(Color.GREEN)
print("Zielone produkty:")
for p in bf.filter(products, green):
    print(f"{p.name} jest zielony.")

# Zapytanie o nowe filtrowanie z biznesu

class SizeSpecification(Specificaion):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

print("Duże produkty")
large = SizeSpecification(Size.LARGE)
for p in bf.filter(products, large):
    print(f"{p.name} jest duży")

##################################

class AndSpecification(Specificaion):
    def __init__(self, spec1, spec2):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied(self, item):
        return self.spec1.is_satisfied(item) and self.spec2.is_satisfied(item)

print("Producty zielone i duże")
large_blue = SizeSpecification(Size.LARGE) and ColorSpecification(Color.BLUE)

for p in bf.filter(products, large_blue):
    print(f"{p.name} jest niebieski i duży")