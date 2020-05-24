# ISP - Zasada rozdzielenia interfejsów
# Złamanie ISP

class Machine:
    def print_doc(self, doc):
        NotImplementedError

    def scan(self, doc):
        NotImplementedError

    def fax(self, doc):
        NotImplementedError


class MultiFunctionPrinter(Machine):
    def print_doc(self, doc):
        print(f"Drukuję {doc}")

    def scan(self, doc):
        print(f"Skanuję {doc}")

    def fax(self, doc):
        print(f"Wysyłam fax {doc}")

m = MultiFunctionPrinter()
m.print("mój_dokument")


class OldFashionedPrinter(Machine):
    def print_doc(self, doc):
        print(f"Drukuję po staremu {doc}")

    def fax(self, doc):
        raise NotImplementedError("Printer cannot fax")

    def scan(self, doc):
        raise NotImplementedError("Printer cannot scan")

o = OldFashionedPrinter()
o.scan("moj_dokument")

# Zasada ISP zachowana

import abc

class Printer(abc.ABC):

    @abc.abstractmethod
    def print_doc(self, doc):
        pass

class Scan(abc.ABC):

    @abc.abstractmethod
    def scan(self, doc):
        pass

class Fax(abc.ABC):

    @abc.abstractmethod
    def fax(self, doc):
        pass

class OldFashionedPrinter2(Printer):
    def print_doc(self, doc):
        print(f"OldFashionedPrinter drukuje {doc}")


class PhotoCopier(Printer, Scan):
    def print_doc(self, doc):
        print(f"PhotoCopier drukuje {doc}")

    def scan(self, doc):
        print(f"PhotoCopier skanuje {doc}")


p1 = OldFashionedPrinter2()
p2 = PhotoCopier()


class MultiFunctionedPrinter(Printer, Scan, Fax):
    def print_doc(self, doc):
        print(f"MultiFunctionedPrinter drukuje {doc}")

    def scan(self, doc):
        print(f"MultiFunctionedPrinter skanuje {doc}")

    def fax(self, doc):
        print(f"MultiFunctionedPrinter wysyła fax {doc}")