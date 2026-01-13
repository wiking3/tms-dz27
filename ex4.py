#  Создать класс Книга с атрибутами : название, автор и год издания. Создать методы для получения и изменения этих атрибутов. Создать объекты и вызвать данные методы.
class Book:
    def __init__(self, name, author, year_of_publication):
        self.name = name
        self.author = author  
        self.year_of_publication = year_of_publication 
        print(f"Книга: {self.name}, Автор: {self.author} Год публикации:{self.year_of_publication} ")


    def get_name(self):
        return self.name
    
    def get_author(self):
        return self.author
    
    def get_year_of_publication(self):
        return self.year_of_publication
    
    def set_name(self, new_name):
        print (f"Для книги {self.name} -- Имя книги изменено на : {new_name}")
        self.name = new_name 
    
    def set_author(self, new_author):
        print (f"Для книги {self.name} -- Автор изменен на : {new_author}")
        self.author = new_author 

    def set_year_of_publication(self, new_year_of_publication):
        print (f"Для книги {self.name} -- Год публикации изменен на : {new_year_of_publication}")
        self.year_of_publication = new_year_of_publication

    
book1 = Book("Book-1","Konan Doil", "1980")
book2 = Book("Book-2","Teodor Draizer", "1982")
book3 = Book("Book-3","Nick Perumov", "1992")


print( f"{book1.get_name()} -- {book1.get_author()} -- {book1.get_year_of_publication()}" )
print( f"{book2.get_name()} -- {book2.get_author()} -- {book2.get_year_of_publication()}" )
print( f"{book3.get_name()} -- {book3.get_author()} -- {book3.get_year_of_publication()}" )

book1.set_name ("Book-100")
book1.set_author ("Lev Tolstoj")
book1.set_year_of_publication("2020")

book2.set_name ("Book-20")
book2.set_author ("Fedor Dostoevkij")
book2.set_year_of_publication("2002")

print( f"\n После изменений : " )
print( f"{book1.get_name()} -- {book1.get_author()} -- {book1.get_year_of_publication()}" )
print( f"{book2.get_name()} -- {book2.get_author()} -- {book2.get_year_of_publication()}" )
print( f"{book3.get_name()} -- {book3.get_author()} -- {book3.get_year_of_publication()}" )
