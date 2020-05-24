from computer import Computer
from abs_computer import AbsComputer

class MyComputer(AbsComputer):

    def get_computer(self):
        return self._computer

    def get_case(self):
        self._computer.case = "Coolmaster N300"
        return self

    def get_mainboard(self):
        self._computer.mainboard = "MSI 978"
        self._computer.cpu = "Intel Core i7-4778"
        self._computer.memory = "Corsair Vengeance 16GB"
        return self

    def install_hard_disk(self):
        self._computer.hard_disk = "Seagate 2TB"
        return self