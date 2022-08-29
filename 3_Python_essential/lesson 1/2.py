class Book:

    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre
        self.reviews = []

    def __str__(self):
        output = f"Author: {self.author}, Title: {self.title}, Year: {self.year}, Genre: {self.genre}."
        if self.reviews:
            output = output + "\nWe found " + str(len(self.reviews)) + " reviews for this book:\n"
            for review in self.reviews:
                output = output + "\n" + ("*" * review.score) + "\n" + review.review
            return output
        else:
            return output

    def __repr__(self):
        return f"Author: {self.author}, Title: {self.title}, Year: {self.year}, Genre: {self.genre}."

    def review(self):
        new_review = Review(self)
        self.reviews.append(new_review)


class Review:

    def __init__(self, book):
        self.book = book
        self.score = int(input("Rate the book from 1 to 5: "))
        self.review = input("Share your thoughts about the book: ")

    def __str__(self):
        return f"You've reviewed the book:\n" \
               f"Author: {self.book.author}, Title: {self.book.title}, Year: {self.book.year}, Genre: {self.book.genre}." \
               f"Your rated it {self.score} stars and provided the following feedback:\n{self.review}"


book1 = Book("Roger Zelazny", "Nine Princes in Amber", 1970, "fantasy")
book2 = Book("Roger Zelazny", "...And Call Me Conrad", 1966, "fantasy")
book3 = Book("Frank Herbert", "Dune", 1966, "fantasy")

print(book1)
book1.review()
book1.review()
print(book1)
