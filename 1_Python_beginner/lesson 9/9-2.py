def main():
    phrase = input("Enter your phrase to palindrome check: ").lower()
    phrase = phrase.replace(" ", "")
    phrase = phrase.replace(",", "")

    if palindrome(phrase):
        print("Yes, it's a palindrome")
    else:
        print("No, this is not a palindrome")


def palindrome(text):
    """This function checks whether text is a palindrome"""
    if text == text[::-1]:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
