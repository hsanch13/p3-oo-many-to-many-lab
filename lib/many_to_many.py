class Author:
    all_authors = []

    def __init__(self, name): 
        self.name = name
    
    def contracts(self):
        return [contract for contract in Contract.all if self is contract.author]
    
    def books(self):
        return list({contract.book for contract in self.contracts()})
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])
    
class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        type(self).all_books.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if self is contract.book]
    
    def authors(self):
        return list({contract.author for contract in self.contracts()})

    

class Contract:
    all = []

    def __init__(self, author, book, date, royalties): 
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        type(self).all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception()
        
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception()
        
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise Exception()
        
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise TypeError("value should be an interger")

    @classmethod
    def contracts_by_date(cls, date):
        """returns a list of contracts by a specific date of type string"""
        return [contract for contract in cls.all if contract.date == date]
    


# author1 = Author("Name 1")
# book1 = Book("Title 1")
# book2 = Book("Title 2")
# book3 = Book("Title 3")
# author2 = Author("Name 2")
# book4 = Book("Title 4")
# contract1 = Contract(author1, book1, "02/01/2001", 10)
# contract2 = Contract(author1, book2, "01/01/2001", 20)
# contract3 = Contract(author1, book3, "03/01/2001", 30)
# contract4 = Contract(author2, book4, "01/01/2001", 40)   

# import ipdb;ipdb.set_trace()