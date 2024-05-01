import tkinter as tk 
from tkinter.ttk import Treeview
from Components import Book
from DataLayer import DALBook

class frmBookslist:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("List Of Books")
        self.root.geometry("600x400")
        
        self.tree1 = Treeview(self.root)
        self.tree1['columns']=('c1','c2')
        
        self.tree1.heading('#0',text='Book Id')
        self.tree1.heading('c1',text='Book Name')
        self.tree1.heading('c2',text='Author Name')
        
        objDAL = DALBook()
        AllBooks=objDAL.getBooks()
        
        i=0 
        
        for Book in AllBooks:
            self.tree1.insert('',1,text=Book.BookId,values=(Book.BookName,Book.Author))
            i+=1 
        self.tree1.pack()
        self.root.mainloop()

obj = frmBookslist()