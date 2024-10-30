#SRP #SOC

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

j = Journal()
j.add_entry('He cried today.')
j.add_entry('He ate a big cake.')
print(f"Journal Entries:\n{j}")
