import turtle
import tkinter as tk
from cardOld import *

class GameWindow:
    def __init__(self):
        self.screen = turtle.Screen()
        self.canvas = self.screen.getcanvas()
        self.screen.bgcolor("green")
        #self.screen.setup(800,650)
        self.screen.title("Calculation")
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.hideturtle()

        self.foundations = []
        self.wastes = []
        self.foundButtons = []
        self.wasteButtons = []
        self.foundButtons.append(tk.Button(self.canvas.master, text = "Play Here",command=lambda:[self.foundationPlay(0)],state="disabled"))
        self.foundButtons.append(tk.Button(self.canvas.master, text = "Play Here",command=lambda:[self.foundationPlay(1)],state="disabled"))
        self.foundButtons.append(tk.Button(self.canvas.master, text = "Play Here",command=lambda:[self.foundationPlay(2)],state="disabled"))
        self.foundButtons.append(tk.Button(self.canvas.master, text = "Play Here",command=lambda:[self.foundationPlay(3)],state="disabled"))
        self.wasteButtons.append(tk.Button(self.canvas.master, text = "Play Here",command=lambda:[self.wastePlay(0)],state="disabled"))
        self.wasteButtons.append(tk.Button(self.canvas.master, text = "Play Here",command=lambda:[self.wastePlay(1)],state="disabled"))
        self.wasteButtons.append(tk.Button(self.canvas.master, text = "Play Here",command=lambda:[self.wastePlay(2)],state="disabled"))
        self.wasteButtons.append(tk.Button(self.canvas.master, text = "Play Here",command=lambda:[self.wastePlay(3)],state="disabled"))
        self.scoreButton = tk.Button(self.canvas.master, text="Calculate Score", command=self.calculateScore)    
        for i in range(4):
            self.foundations.append(Pile(i+1))
            self.wastes.append(Pile())
            

        self.cardToPlay = Card("","")
        self.wasteNum = -1
        self.deck = Deck()
        self.deck.shuffle()
        self.foundationSetup()

        card = Card("","")
        card.render(-250,-200,self.pen)
        start_x = -250
        for x in range(4):
            card = self.foundations[x].cards[self.foundations[x].topCard]
            card.render(start_x + x *125, 200,self.pen)
            if self.wastes[x].topCard > -1:
                card = self.wastes[x].cards[self.wastes[x].topCard]
            else:
                card = Card("","")
            card.render(start_x + x *125, 25,self.pen)
        self.drawButton = tk.Button(self.canvas.master, text="Draw Card", command=self.drawCard)
        self.canvas.create_window(-250,300,window=self.drawButton)
        for i in range(4):
            self.canvas.create_window(-250 + 125*i,-300,window=self.foundButtons[i])
            self.canvas.create_window(-250 + 125*i,75,window=self.wasteButtons[i])

    def foundationSetup(self):
        for card in self.deck.cards:
            if card.rank == "A":
                self.deck.cards.remove(card)
                self.foundations[0].playCard(card)
                break
        for card in self.deck.cards:
            if card.rank == "2":
                self.deck.cards.remove(card)
                self.foundations[1].playCard(card)
                break
        for card in self.deck.cards:
            if card.rank == "3":
                self.deck.cards.remove(card)
                self.foundations[2].playCard(card)
                break
        for card in self.deck.cards:
            if card.rank == "4":
                self.deck.cards.remove(card)
                self.foundations[3].playCard(card)
                break
    def wasteButtonDisplay(self):
        for i in range(4):
            if self.wastes[i].topCard > -1:
                self.wasteButtons[i]["text"] = "Play Card"
                self.wasteButtons[i]["state"] = "normal"
            else:
                self.wasteButtons[i]["state"] = "disabled"
        if len(self.deck) == 0:
            self.drawButton["state"] = "disabled"
            self.canvas.create_window(-250 + 125*3,150,window=self.scoreButton)
    def drawCard(self):
        self.wasteNum = -1
        self.cardToPlay = self.deck.deal()
        self.cardToPlay.render(-250,-200, self.pen)
        self.drawButton["state"] = "disabled"
        for i in range(4):
            self.foundButtons[i]["state"] = "normal"
            self.wasteButtons[i]["text"] = "Play Here"
            self.wasteButtons[i]["state"] = "normal"
    def foundationPlay(self,num):
        if self.foundations[num].playCard(self.cardToPlay):
            self.cardToPlay = Card("","")
            self.foundations[num].cards[self.foundations[num].topCard].render(-250 + 125*num, 200,self.pen)
            if self.wasteNum == -1:
                self.cardToPlay.render(-250,-200,self.pen)
            elif self.wastes[self.wasteNum].topCard > -1:
                self.wastes[self.wasteNum].cards[self.wastes[self.wasteNum].topCard].render(-250 + 125*self.wasteNum,25,self.pen)
            else:
                 self.cardToPlay.render(-250 + self.wasteNum*125,25,self.pen)
            for i in range(4):
                self.foundButtons[i]["state"] = "disabled"
            self.drawButton["state"] = "normal"
            self.wasteButtonDisplay()
        elif self.wasteNum != -1:
            self.wastes[self.wasteNum].playCard(self.cardToPlay)
            self.cardToPlay = Card("","")
            for i in range(4):
                self.foundButtons[i]["state"] = "disabled"
       
            self.drawButton["state"] = "normal"
            self.wasteButtonDisplay()
    def wastePlay(self,num):
        if self.cardToPlay.rank != "":
            self.wastes[num].playCard(self.cardToPlay)
            self.cardToPlay = Card("","")
            for i in range(4):
                self.foundButtons[i]["state"] = "disabled"
            self.drawButton["state"] = "normal"
            self.cardToPlay.render(-250,-200,self.pen)
            self.wastes[num].cards[self.wastes[num].topCard].render(-250+125*num,25,self.pen)
            self.wasteButtonDisplay()
        else:
            self.cardToPlay = self.wastes[num].getTopCard()
            self.drawButton["state"] = "disabled"
            for i in range(4):
                self.foundButtons[i]["state"] = "normal"
                self.wasteButtons[i]["state"] = "disabled"
            self.wasteNum = num    
    def calculateScore(self):
        score = 0
        for i in range(4):
            score += len(self.wastes[i])
        self.pen.penup()
        self.pen.goto(-125,-100)
        self.pen.write("Score: "+ str(score),False,font=("Courier New", 48,"normal"))


             

if __name__ == '__main__':
    
    GameWindow().screen.mainloop()

        