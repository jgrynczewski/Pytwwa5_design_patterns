from my_computer import MyComputer
from cheap_computer import CheapComputer
from director import Director

builder = MyComputer()
director = Director(builder)
director.build_computer()
computer = director.get_computer()
computer.display()


