#SRP #SOC
from fileinput import filename


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    # This method breaks the SRP
    def save(self, filename):
        file = open(filename, 'w')
        file.write(str(self))
        file.close()

    # This method breaks the SRP
    def load(self, filename):
        pass

    # This method breaks the SRP
    def load_from_web(self, uri):
        pass
# These ones give additional responsibilities to Journal class
# to fix it, we can seperate these funcs and implement them in a more global class

class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()

j = Journal()
j.add_entry('He cried today.')
j.add_entry('He ate a big cake.')
print(f"Journal Entries:\n{j}")

fl = 'testing.txt'
PersistenceManager.save_to_file(j,fl)

with open(fl) as fh:
    print(fh.read())

# There must be single reason to change for  a class