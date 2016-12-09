class Book:
    '''
    Simple class just used to demonstrate testing
    '''

    def __init__(self, title, author):
        '''
        Creates a new Book object

        :param title: Title of the book
        :param author: Author of the book
        :return: returns nothing
        '''
        self.title = title
        self.author = author
        self.pages = 0

    def setPages(self, num):
        '''
        Sets the number of pages for the book

        :param num: Number of pages
        :return: returns nothing
        '''
        self.pages = num

    def __str__(self):
        '''
        Overrided __str__ function to make printing the object prettier
        '''
        mystring = "Author: " + self.author + '\n'
        mystring += "Title: " + self.title + '\n'
        mystring += "Pages: " + str(self.pages) + '\n'
        return mystring
