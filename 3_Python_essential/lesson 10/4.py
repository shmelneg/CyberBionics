import re


def words_counter(text):
    words = re.sub(r'[,;?:!.]', "", text).lower().split()
    unique_words = set()
    for word in words:
        unique_words.add(word)
    print(f"There are {len(words)} words in your phase and {len(unique_words)} of them are unique")
    print("The unique words are:", unique_words)


phrase = input("Enter a phrase or several words: ")

words_counter(phrase)
