import abc

class AbsStrategy(abc.ABC):

    @abc.abstractmethod
    def calculate(self):
        """Calculate shipping cost"""