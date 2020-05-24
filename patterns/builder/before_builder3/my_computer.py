from computer import Computer

class MyComputer:

    def get_computer(self):
        return self._computer

    def build_computer(self):
        self._computer = Computer()
        self.get_case()
        self.get_mainboard()
        self.install_hard_drive()

    def get_case(self):
        self._computer.case = "Coolmaster N300"

    def get_mainboard(self):
        self._computer.mainboard = "MSI 978"
        self._computer.cpu = "Intel Core i7-4778"
        self._computer.memory = "Corsair Vengeance 16GB"

    def install_hard_drive(self):
        self._computer.hard_disk = "Seagate 2TB"