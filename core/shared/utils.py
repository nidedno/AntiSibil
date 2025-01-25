from tkinter import messagebox
import os, json, glob
from .constants import ACCOUNTS_FOLDER
from ..logic.account import Account

# Loads all existing accounts
def import_accounts():
    accounts = []
    for filename in glob.glob(os.path.join(ACCOUNTS_FOLDER, '*.json')):
        with open(filename, 'r') as f:
            account_text = f.read()
            account_json = json.loads(account_text)

            name = account_json.get("name", "None")
            account = Account(name=name, fields=account_json)
            print(account)
            accounts.append(account)

    if (len(accounts) == 0):
        raise Exception("No accounts found.")
    
    return accounts

def read_json(file):
    with open(file, 'r') as f:
        text = f.read()
        json_data = json.loads(text)
        return json_data
    
    raise Exception("No json found.")