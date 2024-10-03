import random
import turtle
# Card drawing is based on the Deck of Cards Simulator by @TokyoEdtech
# https://github.com/wynand1004/Projects/blob/master/Cards/deck_of_cards.py
# Combo of Turtle and tkinter based on code from
# https://compucademy.net/python-turtle-graphics-and-tkinter-gui-programming/

class Card(object):
    """A card object with a suit and rank."""

    RANKS = ("A","2","3","4","5","6","7","8","9","10","J","Q","K","")
    SUITS = ("Spades", "Diamonds", "Hearts", "Clubs","")
    SUIT_SYMBOL = {"Diamonds":"♦", "Clubs":"♣", "Hearts":"♥", "Spades":"♠"}

    def __init__(self,rank:str,suit:str):
        """Creates a card with the given rank and suit."""
        if rank in Card.RANKS:
           self.rank = rank 
        else:    
            raise Exception("Rank must be between 0 and 12")
        if suit in Card.SUITS:
            self.suit = suit
        else:
            raise Exception("Suit must be Spades, Diamonds, Hearts, or Clubs")
    def __str__(self):
        """Returns the strign representation of a card"""
        return self.rank + Card.SUIT_SYMBOL[self.suit]
    def render(self, x:int, y:int, pen:turtle.Turtle):
        #draw border
        pen.penup()
        pen.goto(x,y)
        pen.color("white")
        pen.goto(x-50, y+75)
        pen.begin_fill()
        pen.pendown()
        pen.goto(x+50, y+75)
        pen.goto(x+50,y-75)
        pen.goto(x-50,y-75)
        pen.goto(x-50,y+75)
        pen.end_fill()
        pen.penup()

        if self.rank != "":
            if self.suit == "Diamonds" or self.suit == "Hearts":
                pen.color("red")
            else:
                pen.color("black")
            pen.goto(x-18,y-30)
            pen.write(Card.SUIT_SYMBOL[self.suit],False,font=("Courier New", 48,"normal"))

            #top left
            pen.goto(x-40, y+45)
            pen.write(self.rank, False,font=("Courier New", 18, "normal"))
            pen.goto(x-40,y+25)
            pen.write(Card.SUIT_SYMBOL[self.suit],False,font=("Courier New",18, "normal"))
            
            #bottom right
            pen.goto(x+40,y-60)
            
            pen.write(self.rank, False,align="right",font=("Courier New", 18, "normal"))
            pen.goto(x+40, y-80)
            pen.write(Card.SUIT_SYMBOL[self.suit], False,align="right",font=("Courier New", 18, "normal"))

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
        
        