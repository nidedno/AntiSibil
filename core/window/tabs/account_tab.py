import tkinter as tk
from tkinter import ttk
from ...shared.utils import import_accounts

# Create accounts tabs with tree view.
def create_accounts_tab(notebook):
    tab_accounts = ttk.Frame(notebook)
    notebook.add(tab_accounts, text='Accounts')

    # Add header
    header_frame = tk.Frame(tab_accounts, bg="white")
    header_frame.pack(fill=tk.X)

    # Add label
    header_label = tk.Label(header_frame, text="Accounts", bg="white", font=("Arial", 12))
    header_label.pack(side=tk.LEFT, padx=5, pady=0)

    # Add button on right
    add_button = tk.Button(header_frame, text=" + ", bg="green", fg="white", font=("Arial", 12), command=add_acount)
    add_button.pack(side=tk.RIGHT, padx=10, pady=5)

    try:
        accounts = import_accounts()
    except:
        ttk.Label(tab_accounts, text="Here's no accounts for now, try create a new accounts.").pack(padx=10, pady=10)
    else:
        print(1)

def add_acount():
    print(3)

def accounts_tab_refresh():
    print(2)