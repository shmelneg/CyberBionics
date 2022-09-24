import abc
import random


class Deck:

    def __init__(self):
        self.suits = ["♣", "♦", "♥", "♠"]
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.deck = self.deck_generate()

    def deck_generate(self):
        cards = []
        for rank in self.ranks:
            for suit in self.suits:
                cards.append(rank + suit)
        return cards

    def shuffle(self):
        random.shuffle(self.deck)

    def get_top_card(self):
        return self.deck.pop(-1)


class AbstractPlayer(abc.ABC):

    def __init__(self):
        self.cards = []
        self.points = 0
        self.active = True
        self.name = "Person"

    def take_card(self, card):
        self.cards.append(card)
        if card[0] == "A":
            if (self.points + 11) <= 21:
                self.points += 11
            else:
                self.points += 1
        elif card[0] in ["J", "Q", "K"] or card[0:2] == "10":
            self.points += 10
        else:
            self.points += int(card[0])

    @abc.abstractmethod
    def ask_card(self):
        pass

    def __str__(self):
        return f"{self.name}'s cards: {self.cards}\n{self.name}'s points: {self.points}"

class Player(AbstractPlayer):

    def __init__(self):
        super().__init__()
        self.name = "Player"

    def ask_card(self):
        choice = input("Do you want to take another card? ").lower()
        if choice == "y" or choice == "yes":
            return True
        else:
            self.active = False
            print("Player stops")
            return False


class Dealer(AbstractPlayer):

    def __init__(self):
        super().__init__()
        self.name = "Dealer"

    def ask_card(self):
        if self.points < 17:
            return True
        else:
            self.active = False
            print("Dealer stops")
            return False
