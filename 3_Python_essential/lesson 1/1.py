class Book:

    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre

    def __str__(self):
        return f"Author: {self.author}, Title: {self.title}, Year: {self.year}, Genre: {self.genre}."

    def __repr__(self):
        return f"Author: {self.author}, Title: {self.title}, Year: {self.year}, Genre: {self.genre}."

    def same_author(self, another):
        if self.author == another.author:
            return True
        else:
            return False

    def same_year(self, another):
        if self.year == another.year:
            return True
        else:
            return False

    def same_genre(self, another):
        if self.genre == another.genre:
            return True
        else:
            return False

book1 = Book("Roger Zelazny", "Nine Princes in Amber", 1970, "fantasy")
book2 = Book("Roger Zelazny", "...And Call Me Conrad", 1966, "fantasy")
book3 = Book("Frank Herbert", "Dune", 1966, "fantasy")

print(book1)
print(book2)
print(book3)

if book2.same_year(book3):
    print(f"{book2.author} wrote his book '{book2.title}' the same year when {book3.author} wrote '{book3.title}'")
