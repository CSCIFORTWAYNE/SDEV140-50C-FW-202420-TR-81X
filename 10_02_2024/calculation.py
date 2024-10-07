from breezypythongui import EasyCanvas, EasyFrame, EasyDialog
from card import *
import tkinter as tk


#other imports

class CalculationGame(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, width=1200, height=600)
        self.game = GamePlayArea(self)
        self.addCanvas(self.game, row=0, column=0, columnspan=2)
        # add other widgets to the window
    #Add definitions of event handlers
class GamePlayArea(EasyCanvas):
    def __init__(self, parent):
        EasyCanvas.__init__(self, parent, background="green")
        self.foundations = list()
        self.wastes = list()
        for i in range(4):
            self.foundations.append(Pile(i+1))
            self.wastes.append(Pile())
        self.deck = Deck()
        self.deck.shuffle()
        self.cardPlace = Card("", "")
        self.cardToPlay = self.cardPlace
        self.wasteNum = -1
        self.foundationSetup()
        self.cardPlace.render(275,500,self)
        start_x = 150
        for x in range(4):
            card = self.foundations[x].cards[self.foundations[x].topCard]
            card.render(start_x + x*125, 100, self)
            if self.wastes[x].topCard > -1:
                card = self.wastes[x].cards[self.wastes[x].topCard]
            else:
                card = Card("", "")
            card.render(start_x + x*125, 300, self)
        self.drawButton = tk.Button(self.master, text="Draw Card", command=self.drawCard)
        self.create_window(150,500,window=self.drawButton)
        self.scoreButton = tk.Button(self.master, text="Calculate Score", command=self.calculateScore)
        self.create_window(150 + 125*3,500,window=self.scoreButton)
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
    def drawCard(self):
        self.wasteNum = -1
        self.cardToPlay = self.deck.deal()
        self.cardToPlay.render(275,500, self)
        self.drawButton["state"] = "disabled"

    def calculateScore(self):
        self.score = 0
        for i in range(4):
            self.score += len(self.wastes[i])
        dialog = tk.messagebox.askyesnocancel(title="Game Over", message=f"Final Score {self.score}\nDo you want to play again?")
        if dialog:
            self.master.game.destroy()
            self.master.game = GamePlayArea(self.master)
            self.master.addCanvas(self.master.game,row=0, column=0, columnspan=2)
        elif dialog == False:
            self.master.winfo_toplevel().destroy()
    def mousePressed(self, event):
        self.x = event.x
        self.y = event.y
        
        self.selectedItem = self.findClickedItem(self.x, self.y)
        print(self.selectedItem)
        if self.selectedItem != None:
            self.tag_raise(self.selectedItem.rectangle)
            self.tag_raise(self.selectedItem.upperLeft)
            self.tag_raise(self.selectedItem.lowerRight)
            self.tag_raise(self.selectedItem.suitSymbol)

    def mouseDragged(self,event):
        if self.selectedItem:
            xDistance = event.x - self.x
            yDistance = event.y - self.y
            self.move(self.selectedItem.rectangle, xDistance, yDistance)
            self.move(self.selectedItem.upperLeft, xDistance, yDistance)
            self.move(self.selectedItem.lowerRight, xDistance, yDistance)
            self.move(self.selectedItem.suitSymbol, xDistance, yDistance)
            self.x = event.x
            self.y = event.y
    def mouseReleased(self, event):
        if self.selectedItem == None:
            return
        foundationDrop = self.findFoundation(event.x, event.y)
        if foundationDrop != None:
            card = foundationDrop.cards[foundationDrop.topCard]
            coords = self.coords(card.rectangle)
            if foundationDrop.playCard(self.selectedItem):
                self.delete(self.selectedItem.rectangle)
                self.delete(self.selectedItem.lowerRight)
                self.delete(self.selectedItem.upperLeft)
                self.delete(self.selectedItem.suitSymbol)
                self.selectedItem.render(coords[0]+50, coords[1]+75, self)
                if self.selectedItem == self.cardToPlay:
                    self.cardToPlay = self.cardPlace
                    self.drawButton["state"] = "normal"
            elif self.selectedItem == self.cardToPlay:
                self.delete(self.selectedItem.rectangle)
                self.delete(self.selectedItem.lowerRight)
                self.delete(self.selectedItem.upperLeft)
                self.delete(self.selectedItem.suitSymbol)
                self.selectedItem.render(275,500, self)
            else:
                self.delete(self.selectedItem.rectangle)
                self.delete(self.selectedItem.lowerRight)
                self.delete(self.selectedItem.upperLeft)
                self.delete(self.selectedItem.suitSymbol)
                self.selectedItem.render(150+self.wasteNum*125,300,self)
                self.wastes[self.wasteNum].playCard(self.selectedItem)
        elif self.selectedItem == self.cardToPlay:
            wasteDrop = self.findWaste(event.x, event.y)
            if wasteDrop == None:
                self.delete(self.selectedItem.rectangle)
                self.delete(self.selectedItem.lowerRight)
                self.delete(self.selectedItem.upperLeft)
                self.delete(self.selectedItem.suitSymbol)
                self.selectedItem.render(275,500, self)
            else:
                self.deleteSelectedItem()
                self.selectedItem.render(150+self.wasteNum*125,300,self)
                self.wastes[self.wasteNum].playCard(self.selectedItem)
                self.drawButton["state"] = "normal"
                self.cardToPlay = self.cardPlace
        
        else:
            self.deleteSelectedItem()
            self.selectedItem.render(150+self.wasteNum*125,300,self)
            self.wastes[self.wasteNum].playCard(self.selectedItem)

        self.selectedItem = None
        wasteNum = -1
        """ if len(self.deck) == 0 and self.cardToPlay.rank == "":
            self.drawButton["state"] = "disabled"
            self.create_window(150 + 125*3,500,window=self.scoreButton) """


    def findClickedItem(self, x,y):
        if self.cardToPlay.rank != "":
            coords = self.coords(self.cardToPlay.rectangle)
            if self.containsPoint(coords, x, y):
                return self.cardToPlay
        for i in range(4):
            if self.wastes[i].topCard != -1:
                topCard = self.wastes[i].getTopCard()
                coords = self.coords(topCard.rectangle)
                if self.containsPoint(coords, x, y):
                    self.wasteNum = i
                    return topCard
                else:
                    self.wastes[i].playCard(topCard)
    def findFoundation(self, x, y):
        for foundation in self.foundations:
            topCard = foundation.getTopCard()
            coords = self.coords(topCard.rectangle)
            foundation.playCard(topCard)
            if self.containsPoint(coords, x, y):
                return foundation
        return None
    def findWaste(self, x, y):
        for i in range(4):
            if self.wastes[i].topCard == -1:
                coords = [75+i*125, 150, 225 + i*125, 450]
            else:
                card = self.wastes[i].cards[self.wastes[i].topCard]
                coords = self.coords(card.rectangle)
            if self.containsPoint(coords, x, y):
                self.wasteNum = i
                return self.wastes[i] 
    
    def containsPoint(self, coords, x, y):
        [x0, y0, x1, y1] = coords
        print(x,y, x0,y0, x1,y1)
        return x >= min(x0,x1) and x <= max(x0,x1) and y >= min(y0, y1) and y <= max(y0, y1)
    def deleteSelectedItem(self):
        self.delete(self.selectedItem.rectangle)
        self.delete(self.selectedItem.lowerRight)
        self.delete(self.selectedItem.upperLeft)
        self.delete(self.selectedItem.suitSymbol)
        

def main():
    CalculationGame().mainloop()

if __name__ == "__main__":
    main()