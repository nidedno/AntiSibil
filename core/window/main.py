import tkinter as tk
from .menu.main_menu import create_main_menu
from .menu.tabs_menu import create_tabs

def start():
    root = tk.Tk()
    root.title("AutoSibil")
    root.geometry("800x600")

    # main_menu
    create_main_menu(root)

    # tabs
    create_tabs(root)

    root.mainloop()
    