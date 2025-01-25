import tkinter as tk
from tkinter import ttk

def create_tabs(root):
    # Создание виджета Notebook
    notebook = ttk.Notebook(root)

    create_accounts_tab(notebook)
    create_projects_tab(notebook)
    create_scenarios_tab(notebook)
    create_activity_tab(notebook)

    notebook.pack(expand=True, fill="both", side="top")
    root.mainloop()


# Create accounts tabs
def create_accounts_tab(notebook):
    tab_accounts = ttk.Frame(notebook)
    ttk.Label(tab_accounts, text="Here will be a list of accounts").pack(padx=10, pady=10)
    
    notebook.add(tab_accounts, text='Accounts') # add tab

# Create projects tab
def create_projects_tab(notebook):
    projects_tab = ttk.Frame(notebook)
    ttk.Label(projects_tab, text="Here will be list of projects").pack(padx=10, pady=10)
    
    notebook.add(projects_tab, text='Projects') # add tab

# Create scenarious tab
def create_scenarios_tab(notebook):
    scenarios_tab = ttk.Frame(notebook)
    ttk.Label(scenarios_tab, text="Here will be list of scenarious").pack(padx=10, pady=10)
    
    notebook.add(scenarios_tab, text='Scenarious')

# Create activity tab
def create_activity_tab(notebook):
    activity_tab = ttk.Frame(notebook)
    ttk.Label(activity_tab, text="Here will be list of acitivty which we can use").pack(padx=10, pady=10)
    
    notebook.add(activity_tab, text='Activity')



