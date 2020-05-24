from my_computer import MyComputer
from cheap_computer import CheapComputer

builder = MyComputer()
builder.build_computer()
computer = builder.get_computer()
computer.display()


