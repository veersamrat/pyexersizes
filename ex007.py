

class BookLibrary:
    no_of_books = 0
    books = []
    
    
    def show_books(self):
        print(f"No of books:{self.no_of_books}")
        print("Books Names are \n")
        for i,x in enumerate(self.books):
            print(f"{i+1}.{x}")
    
         
    def add_book(self,bname):
        self.books.append(bname)
        self.no_of_books += 1
    

def blib():
    chce=int(input('\n1.Show Books \n2.Add book \nEnter your Choice \n'))
    if(chce > 1 and chce < 1):
        print('Invalid Choice')
        blib()
    else:
        match(chce):
            case 1:
               books.show_books()
               blib()
            case 2:
                bname = input("Enter Book Name\n")
                books.add_book(bname)
                print('Book added Successfully\n')
                blib()
            case _:blib()
            
books=BookLibrary()   
print("Welcome to Library ")
blib()
                
                
               
        
    
        