import pyjokes
from colorama import Fore, Style
import random


def main():
    print(Fore.RED + "Hi! I'm a simple chat bot. I can't do a lot yet but I can tell you a joke "
                     "or play a quick game with you.")
    print(Style.RESET_ALL)
    while True:
        answer = input("- What would you like to do?\n- ").lower().split()
        if "joke" in answer:
            print("Here is a top-notch joke:")
            print(Fore.RED + pyjokes.get_joke())
            print(Style.RESET_ALL, end='')
            print('🤣')
        elif "game" in answer:
            rock_paper_scissors()
        elif ("exit" in answer) or ("quit" in answer) or ("stop" in answer):
            print("Goog Bye!")
            break
        else:
            print("I can't understand what you're saying. As I have said I am only able to tell a JOKE "
                  "or play a GAME. Try it. Or if you don't want you always can QUIT.")


def rock_paper_scissors():
    print(Fore.RED + "Let's play ROCK-PAPER-SCISSORS!")
    print(Style.RESET_ALL, end='')
    FIGURES = {'1': '🪨', '2': '📄', '3': '✂'}
    while True:
        bot_figure = random.choice(list(FIGURES.values()))
        while True:
            choice = input("Choose your figure:\n\t1. Rock\n\t2. Paper\n\t3. Scissors\n>> ")
            if choice in list(FIGURES.keys()):
                player_figure = FIGURES[choice]
                break
            else:
                print('Please choose 1, 2, or 3')
        print("Player's figure: " + player_figure)
        print("Bot's figure: " + bot_figure)
        if player_figure == bot_figure:
            print("It's a tie!")
        elif (player_figure == '🪨' and bot_figure == '✂') or (player_figure == '📄' and bot_figure == '🪨') or \
                (player_figure == '✂' and bot_figure == '📄'):
            print("You won!")
        else:
            print('You lose!')
        print('-------------------------------------------')
        again = input("Wanna play again? (type 'no' if you don't)\n")
        if again == 'no':
            break
        print('-------------------------------------------')


if __name__ == "__main__":
    main()
