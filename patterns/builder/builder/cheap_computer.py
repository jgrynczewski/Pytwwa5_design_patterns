from computer import Computer
from abs_computer import AbsComputer

class CheapComputer:

    def get_computer(self):
        return self._computer

    def get_case(self):
        self._computer.case = "Coolmaster N200"

    def get_mainboard(self):
        self._computer.mainboard = "MSI 578"
        self._computer.cpu = "Intel Core i5-4778"
        self._computer.memory = "Corsair Vengeance 4GB"

    def install_hard_drive(self):
        self._computer.hard_disk = "Seagate TB"