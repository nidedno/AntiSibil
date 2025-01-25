from tkinter import messagebox
import os, json, glob
from constants import ACCOUNTS_FOLDER

# Loads all existing accounts
def import_accounts():
    accounts = []
    for filename in glob.glob(os.path.join(ACCOUNTS_FOLDER, '*.json')):
        with open(filename, 'r') as f:
            account_text = f.read()
            account = json.loads(account_text)
            accounts.append(account)
            

    if (len(accounts) == 0):
        raise messagebox.showinfo(message="There no accounts found, try add them ;)")
    
    return accounts