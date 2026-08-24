class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    def __str__(self):
        return f"The title of the book - {self.title}, author - {self.author}, pages - {self.pages}"
    def __len__(self):
        return self.pages
    def __eq__(self, other):
        return isinstance(other, Book) and self.title == other.title and self.author == other.author
    def __lt__(self, other):
        return isinstance(other, Book) and self.pages < other.pages
b1 = Book("title_1", "Tolstoy", 183)
b2 = Book("title_2", "Pushkin", 245)
print(b1)
print(b2)
print(len(b1), len(b2))
print(b1 == b2)
print(b1 < b2)