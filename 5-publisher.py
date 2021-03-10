class publisher:
    def __init__(self):
        print ("Parent class")
class book(publisher):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display(self):
        print("The title of the book is ",self.title)
        print("The author of the book is ",self.author)
class pyton(book):
    def __init__(self,price, pages):
        self.price=price
        self.pages=pages
    def display(self):
        print("The price of the book is ",self.price)
        print("Total pages of the book is ", self.pages)

title = input("Enter title of Book :")
author = input("Enter name of Author : ")
price = input("Enter price of Book :")
page = input("Enter no.of pages : ")
c=book(title,author)
c.display()
c=pyton(price,page)
c.display()
