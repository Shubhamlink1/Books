import pyodbc

from Components import Book

class DALBook:
    def __init__(self):
        self.con = pyodbc.connect("driver={sql server};server=DESKTOP-LT2RR3B\SHUBHAMDATA;database=UserDetails;uid=sa;pwd=abc123#")
        
    def __del__(self):
        if self.con!=None:
            self.con.close()
            self.con = None
            
    def save_book(self, book):
        saved = False
        try:
            cur = self.con.cursor()
            query = "insert into Books values(?,?)"
            row = (book.BookName, book.Author)
            
            cur.execute(query, row)
            self.con.commit()
            saved = True
        except:
            self.con.rollback()
            
        return saved
    
    def getBooks(self):
        AllBooks = []
        cur = self.con.cursor()
        cur.execute('select*from Books')
        records = cur.fetchall()
        
        for record in records:
            b=Book()
            b.BookId=record[0]
            b.BookName=record[1]
            b.Author=record[2]
            
            AllBooks.append(b)
            
        return AllBooks
    