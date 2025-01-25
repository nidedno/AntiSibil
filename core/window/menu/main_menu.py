import tkinter as tk
from tkinter import messagebox

def create_main_menu(root):
    #main menu
    main_menu = tk.Menu(root)
    root.config(menu = main_menu)

    #settings menu
    setting_menu = tk.Menu(main_menu, tearoff=0)
    main_menu.add_cascade(label="Settings", menu=setting_menu)
    
    #settings functions
    setting_menu.add_command(label="About", command=lambda: messagebox.showinfo("info", "AutoSibil для криптообогачения"))

    return main_menu
