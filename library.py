class library():
    def __init__(self, book, author):
        self.book = book
        self.author = author
    
    def branch(self):
        print(f"The book named {self.book}, by {self.author} is present")

class story1(library):
    def __init__(self, book, author, horror):
        super().__init__(book, author)
        self.horror = horror

    def branch(self):
        print(f"The book named {self.book}, by {self.author} is a {self.horror} book")

class story2(library):
    def __init__(self, book, author, mythical):
        super().__init__(book, author)
        self.mythical = mythical

    def branch(self):
        print(f"The book named {self.book}, by {self.author} is a {self.mythical} book")

class story3(library):
    def __init__(self, book, author, romantic):
        super().__init__(book, author)
        self.romantic = romantic

    def branch(self):
        print(f"The book named {self.book}, by {self.author} is a {self.romantic} book")

class poem(library):
    def __init__(self, book, author, poem):
        super().__init__(book, author)
        self.poem = poem

    def branch(self):
        print(f"The book named {self.book}, by {self.author} is a {self.poem} book")

s1 = story1("the_devil", "raman", "horror")
p1 = poem("romeo_juliet", "nick", "romantic")

s1.branch()
p1.branch()