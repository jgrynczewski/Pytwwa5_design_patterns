# DIP - Zasada odwracania zależności

# Złamanie DIP

from enum import Enum

class Relation(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2

class Person:
    def __init__(self, name):
        self.name = name


class Relationship():
    def __init__(self):
        self.relations = []

    def append_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relation.PARENT, child)
             )
        self.relations.append(
            (child, Relation.CHILD, parent)
        )


class Research:
    def __init__(self, relationships):
        data = relationships.relations
        for item in data:
            if item[0].name == "John" and item[1] == Relation.PARENT:
                print(f'{item[2].name} jest dzieckiem {item[0].name}')


p1 = Person("John")
p2 = Person("Chris")
p3 = Person("Matt")
p4 = Person("Paul")
p5 = Person("Ewa")

rs = Relationship()
rs.append_parent_and_child(p1, p2)
rs.append_parent_and_child(p1, p3)
rs.append_parent_and_child(p5, p4)

Research(rs)

# Zachowanie DIP
import abc

class RelationshipBrowser(abc.ABC):
    @abc.abstractmethod
    def find_all_children_of(self, name):
        pass


class Relationship(RelationshipBrowser):
    def __init__(self):
        self.relations = []

    def append_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relation.PARENT, child)
             )
        self.relations.append(
            (child, Relation.CHILD, parent)
        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relation.PARENT:
                yield r[2]


class Research:
    def __init__(self, relationships):
        for item in relationships.find_all_children_of("John"):
            print(f"{item.name} jest dzieckiem Johna.")

print(" ################################ ")

p1 = Person("John")
p2 = Person("Chris")
p3 = Person("Matt")
p4 = Person("Paul")
p5 = Person("Ewa")

rs = Relationship()
rs.append_parent_and_child(p1, p2)
rs.append_parent_and_child(p1, p3)
rs.append_parent_and_child(p5, p4)

Research(rs)