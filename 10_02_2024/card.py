import random
import breezypythongui

class Card:
    """A card object with a suit and rank."""
    RANKS = ("A", "2","3","4","5","6","7","8","9","10","J","Q","K","")
    SUITS = ("SPADES", "DIAMONDS", "HEARTS", "CLUBS","")
    SUIT_SYMBOL = {"DIAMONDS":"♦", "CLUBS":"♣", "HEARTS":"♥", "SPADES":"♠"}

    def __init__(self, rank:str, suit:str):
        if rank.upper() in Card.RANKS:
            self.rank = rank
        else:
            raise ValueError("Rank must be between A and K")
        if suit.upper() in Card.SUITS:
            self.suit = suit.upper()
        else:
            raise ValueError("Suits must be Spades, Diamonds, Hearts, or Clubs")
    def __str__(self):
        return self.rank + Card.SUIT_SYMBOL[self.suit]
    def render(self, x:int, y:int, canvas):
        self.rectangle = canvas.drawRectangle(x-50, y-75, x + 50, y+75, outline="black", fill="white")
        if self.rank != "":
            if self.suit == "DIAMONDS" or self.suit == "HEARTS":
                color = "red"
            else:
                color = "black"
            self.upperLeft = canvas.create_text(x-30, y-50, fill=color, font="Courier 18 normal", text=self.rank)
            self.suitSymbol = canvas.create_text(x, y, fill=color, font="Courier 48 normal", text=Card.SUIT_SYMBOL[self.suit])
            self.lowerRight = canvas.create_text(x+30, y+50, fill=color, font="Courier 18 normal", text=self.rank)

class Deck(object):
    """A deck containing 52 cards."""
    def __init__(self):
        self.cards = []
        for i in range(4):
            for j in range(13):
                c = Card(Card.RANKS[j], Card.SUITS[i])
                self.cards.append(c)
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self):
        if len(self) == 0:
            return None
        else:
            return self.cards.pop()
    def __len__(self):
        return len(self.cards)
    def __str__(self):
        result = ""
        for c in self.cards:
            result = result + str(c) + "\n"
        return result
    
class Pile():
    def __init__(self,num=0):
        self.num = num
        self.sequence = []
        self.cards = []
        self.topCard = -1
        if num != 0:
            for i in range(13):
                self.sequence.append(Card.RANKS[((i+1)*num - 1) % 13])
    def playCard(self, card:Card):
        if self.num == 0 or card.rank == self.sequence[self.topCard + 1]:
            self.cards.append(card)
            self.topCard += 1
            return True
        else:
            return False
    def getTopCard(self):
        self.topCard -=1
        return self.cards.pop()
    def __len__(self):
        return len(self.cards)
