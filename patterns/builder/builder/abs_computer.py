import abc

from computer import Computer


class AbsComputer(abc.ABC):

    def get_computer(self):
        return self._computer()

    def new_computer(self):
        self._computer = Computer()

    @abc.abstractmethod
    def get_case(self):
        pass

    @abc.abstractmethod
    def get_mainboard(self):
        pass

    @abc.abstractmethod
    def install_hard_disk(self):
        pass
