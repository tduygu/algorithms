import random
class Deck:
    cards = []
    def __init__(self):
        pass

    @classmethod
    def getCards(cls):
        Deck.cards.clear()
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        for s in suits:
            for v in values:
                c = Card(s,v)
                Deck.cards.append(c)

    @classmethod
    def shuffle(cls):
        Deck.cards = random.sample(Deck.cards,52)

class Deck1:
    def __init__(self):
        self.cards = []
        self.getCards()

    def getCards(self):
        self.cards.clear()
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        for s in suits:
            for v in values:
                c = Card(s, v)
                self.cards.append(c)

    def shuffle(self):
        self.cards = random.sample(self.cards,len(self.cards))
        # random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            return  None
        else:
            c = self.cards[-1]
            self.cards.pop()
            return c

    def count_remaining(self):
        return len(self.cards)

    def get_remaining(self):
        lst_str = []
        for c in self.cards:
            lst_str.append(c.present())
        return lst_str

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def present(self):
        return f"{self.value} of {self.suit}"




c = Card('hearts', '10')
print(c.present())

#Deck.getCards()
#Deck.shuffle()
#for dc in Deck.cards:
#    print(dc)

d = Deck1()
d.shuffle()
for dc in d.cards:
    print(dc)

print(d.deal())
print(d.deal())
print(d.deal())
print(d.deal())
print(d.deal())
print(d.deal())
print(d.deal())
print(d.deal())
print(d.deal())
print(d.deal())
print(d.deal())
print(d.deal())
print(d.deal())
print(d.deal())
print(d.deal())
print(d.deal())
print(d.count_remaining())
print(d.get_remaining())
