class Book:
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.pages = 0

    def setPages(self, num):
        self.pages = num

    def __str__(self):
        mystring = "Author: " + self.author + '\n'
        mystring += "Title: " + self.title + '\n'
        mystring += "Pages: " + str(self.pages) + '\n'
        return mystring

        

