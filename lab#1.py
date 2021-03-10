import random as rd
import sys
from PyQt5 import QtGui, QtWidgets, uic, QtCore

"""Spider by Evgeny Kolesnikov"""


class Spider(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def show(self):
        print(f"{self.val} of {self.suit}")


class Deck(object):
    _is_face_down = False

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ['Spades']:
            for v in range(1, 14):
                self.cards.append(Spider(s, v))

    @property
    def is_face_down(self):
        return self.is_face_down

    @is_face_down.setter
    def is_face_down(self, value):
        self._is_face_down = value

        if self.is_face_down:
            pixmapback = QtGui.QPixmap('Cards/Spade/green_back.png')
            self.ui.slot1.setPixmap(pixmapback)
        else:
            pixmap3 = QtGui.QPixmap('Cards/Spade/5S.png')
            self.ui.slot3.setPixmap(pixmap3)

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = rd.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()


class SpiderBoard(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.hand = []

        self.ui = uic.loadUi("user_interface.ui")

        self.ui.ShowCards.clicked.connect(self.label_cards)

        self.ui.show()

    def label_cards(self):
        pixmap1 = QtGui.QPixmap('Cards/Spade/AS.png')
        self.ui.slot1.setPixmap(pixmap1)

        pixmap2 = QtGui.QPixmap('Cards/Spade/2S.png')
        self.ui.slot2.setPixmap(pixmap2)

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = SpiderBoard()
    sys.exit(app.exec())


    #deck = Deck()
    #deck.shuffle()
    #deck.show()

    #jack = SpiderBoard("Jack")
    #jack.draw(deck).draw(deck)
    #jack.showHand()