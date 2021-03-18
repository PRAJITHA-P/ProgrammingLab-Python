"""Create a class Publisher (name). Derive class Book from Publisher with attributes title and
author. Derive class Python from Book with attributes price and no_of_pages. Write a
program that displays information about a Python book. Use base class constructor invocation and
method overriding."""


class Publisher:
    def __init__(self, Pubname):
        self.Pubname = Pubname

    def display(self):
        print("Publisher name is:", self.Pubname)


class Book(Publisher):
    def __init__(self, Pubname, title, author):
        Publisher.__init__(self, Pubname)
        self.title = title
        self.author = author

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)


class Python(Book):
    def __init__(self, Pubname, title, author, price, no_of_pages):
        Book.__init__(self, Pubname, title, author)
        self.price = price
        self.no_of_pages = no_of_pages

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Publisher:",self.Pubname)
        print("Price:", self.price)
        print("No of pages:", self.no_of_pages)


b1 = Python("O'Reilly Medi", "Learning Python", "Mark Lutz", 550, 870)
b1.display()
