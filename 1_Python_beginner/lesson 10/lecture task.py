def main():
    text = """Python Tutorial
    Python is a general-purpose interpreted, interactive, object-oriented, and high-level programming language.
    It was created by Guido van Rossum during 1985- 1990. Like Perl, Python source code is also available under
    the GNU General Public License (GPL). This tutorial gives enough understanding on Python programming language.
    Why to Learn Python?
    Python is a high-level, interpreted, interactive and object-oriented scripting language. Python is designed to be
    highly readable. It uses English keywords frequently where as other languages use punctuation, and it has fewer
    syntactical constructions than other languages.
    Audience
    This Python tutorial is designed for software programmers who need to learn Python programming language from 
    scratch.
    Prerequisites
    You should have a basic understanding of Computer Programming terminologies. A basic understanding of any of
    the programming languages is a plus."""

    text_cleared = text.replace(".", "").replace(",", "").replace("?", "").replace("(", "").replace(")", "").lower()
    sep_words = text_cleared.split()
    print("There are", count_words(sep_words), "words in the text.")
    print("The unique words are:", count_unique(sep_words))


def count_words(text):
    return len(text)


def count_unique(text):
    result = {}
    for word in text:
        if word not in result.keys():
            result[word] = 1
        else:
            result[word] += 1
    return result


if __name__ == '__main__':
    main()
