from game_objects import Deck, Dealer, Player


class Game:

    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()

    def start(self):
        print("Let's play Blackjack")
        self.deck.shuffle()
        print("---First round---")
        self.player.take_card(self.deck.get_top_card())
        self.dealer.take_card(self.deck.get_top_card())
        print(self.player)
        print()
        print(self.dealer)

        while self.player.active or self.dealer.active:
            print("---Next round---")
            if self.player.active and self.player.ask_card():
                self.player.take_card(self.deck.get_top_card())
                print(f"Player gets {self.player.cards[-1]}")
                if self.player.points > 21:
                    break
            if self.dealer.active and self.dealer.ask_card():
                self.dealer.take_card(self.deck.get_top_card())
                print(f"Dealer gets {self.dealer.cards[-1]}")
                if self.dealer.points > 21:
                    break
            print(self.player)
            print()
            print(self.dealer)

        print("---Final results---")
        print(self.player)
        print()
        print(self.dealer)
        print("===================")
        if (self.player.points > 21) or (self.player.points < self.dealer.points <= 21):
            print("Sorry, the dealer has won.")
        elif (self.dealer.points > 21) or (self.player.points > self.dealer.points):
            print("Congratulations! You win!")
        else:
            print("It's a tie.")
        print("===================")
