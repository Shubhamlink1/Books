import tkinter as tk
from Components import Book
from DataLayer import DALBook


class frmAddBook:
    def __init__(self):
        self.root = tk.Tk()
        
        self.root.geometry('400x400')
        self.root.title('Add Book')
        
        self.bn = tk.StringVar()
        self.auth = tk.StringVar()
        
        lbl1=tk.Label(self.root,text='Book Name')
        lbl1.place(x=10,y=28)
        
        self.ent1 = tk.Entry(self.root,textvariable = self.bn)
        self.ent1.place(x=90,y=30)
        
        lbl1=tk.Label(self.root,text='Author Name')
        lbl1.place(x=10,y=58)
        
        self.ent2 = tk.Entry(self.root, textvariable=self.auth)
        self.ent2.place(x=90,y=60)
        
        self.btn1 = tk.Button(self.root, text='Save', command = self.save_click)
        self.btn1.place(x=120,y=90)
    
    def show_dialog(self):
        self.root.mainloop()
        
    def save_click(self):
        b = Book()
        b.BookName = self.bn.get()
        b.Author = self.auth.get()
        
        objDAL = DALBook()
        if objDAL.save_book(b)==True:
            print('saved')
        
        objDAL = None
            

obj = frmAddBook()
obj.show_dialog()