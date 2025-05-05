from tkinter import *
from ventana import *

def main():
    root = Tk()
    root.wm_title("Crud Python MySQL")
    root.resizable(False, False)
    root.geometry("1200x600") 
    app = Ventana(root) 
    app.mainloop()

if __name__ == "__main__":
    main()