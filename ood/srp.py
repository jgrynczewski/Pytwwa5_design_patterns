# SRP Single Responsible Principle (SOC - Separation of Concern)
# Zasada jednej odpowiedzialności

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)


class PersitanceManager:

    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()

j = Journal()
j.add_entry("Jestem dzisiaj wesoły")
j.add_entry("Jadę jutro na wycieczkę")

PersitanceManager.save_to_file(j, "journal.txt")

with open("journal.txt", 'r') as f:
    print(f.read())

# God object - antywzorzec