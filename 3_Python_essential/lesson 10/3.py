import re


def main():
    phrase = input("Enter a phrase or several words: ")
    cleared = re.sub(r"[.,;?:!]", "", phrase)
    words = cleared.split()
    last_symbols(words)


def last_symbols(words):
    print("Here are the last 3 symbols of every word from your phrase:")
    for word in words:
        if word == "" or word == " ":
            continue
        elif len(word) <= 3:
            print(word, end=", ")
        else:
            print(word[-3:], end=", ")
    print()


if __name__ == "__main__":
    main()
