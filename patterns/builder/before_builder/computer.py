class Computer:

    def __init__(self, case, mainboard, cpu, memory, hard_disk):
        self.case = case
        self.mainboard = mainboard
        self.cpu = cpu
        self.memory = memory
        self.hard_disk = hard_disk

    def display(self):
        print("Computer:")
        print(f"Case: {self.case}")
        print(f"Mainboard: {self.mainboard}")
        print(f"Cpu: {self.cpu}")
        print(f"Memory: {self.memory}")
        print(f"Hard_disk: {self.hard_disk}")