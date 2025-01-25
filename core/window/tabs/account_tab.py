import tkinter as tk
import os

from tkinter import ttk
from ...shared.utils import import_accounts, read_json
from ...shared.constants import SETTINGS_FOLDER

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
    add_button = tk.Button(header_frame, text=" + ", bg="green", fg="white", font=("Arial", 12), command=lambda: add_acount(notebook))
    add_button.pack(side=tk.RIGHT, padx=10, pady=5)

    try:
        accounts = import_accounts()
    except Exception as e:
        print(e)
        ttk.Label(tab_accounts, text="Here's no accounts for now, try create a new accounts.").pack(padx=10, pady=10)
    else:
        create_accounts_view(tab_accounts, accounts)

def add_acount(notebook):
    print(3)

def accounts_tab_refresh():
    print(2)

def create_accounts_view(notebook, accounts):
    # read all available fields.
    fields = tuple(read_json(SETTINGS_FOLDER + "account.json").keys())
    accounts_tree = ttk.Treeview(notebook)
    accounts_tree["columns"] = fields

    # disable identifier.
    # https://stackoverflow.com/questions/8688839/remove-empty-first-column-of-a-treeview-object
    accounts_tree['show'] = 'headings'

    # Add columns
    for field in fields:
        accounts_tree.column(field)
        accounts_tree.heading(field, text=field)

    # Add
    for account in accounts:
        values = []
        for field in fields:
            if (account.contains_field(field)):
                values.append(account.get(field))
            else:
                values.append("~")
        print(account)
        accounts_tree.insert('', 'end', values=tuple(values))

    accounts_tree.pack(expand=True, fill='both')
