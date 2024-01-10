#wap to create a book class with book name, author name, number of pages, cost and library name, and 
# create three books
#read the details in the main program and pass it to class

class book:
    lname="Parul Library"
    def __init__(self, book_name, author_name, number_of_pages, cost):
        self.book_name = book_name
        self.author_name = author_name
        self.number_of_pages = number_of_pages
        self.cost = cost
    def display(self):
        print("Library Name: ",book.lname,"\n","Book Name: ", self.book_name,"\n","Author Name: ",self.author_name, "\n","Number of Pages: ",self.number_of_pages, "\n","Cost: ",self.cost)

N=int(input("Enter number of books: "))
i=1
while(i<=N):
    book_name=input("Enter Book Name: ")
    author_name=input("Enter Author Name: ")
    number_of_pages=int(input("Enter Number of Pages: "))
    cost=int(input("Enter Cost: "))
    b1=book(book_name, author_name, number_of_pages, cost)
    b1.display()
    print("***************************************************")
    i+=1