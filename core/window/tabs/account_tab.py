import tkinter as tk
from tkinter import ttk

# Create accounts tabs
def create_accounts_tab(notebook):
    tab_accounts = ttk.Frame(notebook)
    ttk.Label(tab_accounts, text="Here will be a list of accounts").pack(padx=10, pady=10)
    notebook.add(tab_accounts, text='Accounts') # add tab