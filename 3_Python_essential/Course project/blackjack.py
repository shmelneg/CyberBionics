from game_logic import Game


def main():
    while True:
        newgame = Game()
        newgame.start()
        replay = input("Do you want to play one more time? ").lower()
        if replay == "y" or replay == "yes":
            continue
        else:
            print("Thank you for the game. Good bye!")
            break


if __name__ == "__main__":
    main()
