import dearpygui.dearpygui as dpg


# utils
from ...shared.utils import import_accounts, read_json
from ...shared.constants import SETTINGS_FOLDER

TAG_ACCOUNTS_TABLE = "Accounts"

# Create accounts tabs with tree view.
def create_accounts_tab():
    with dpg.tab(label="Accounts"):
        dpg.add_spacer()
        
        # Horizontal group.
        with dpg.group(horizontal=True):
            dpg.add_text("Accounts")
            dpg.add_button(label= "+")

        dpg.add_separator()

        # Add table.
        try:
            accounts = import_accounts()
        except Exception as e:
            dpg.add_text("No accounts")
        else:
            create_accounts_table(accounts)

# Create accounts table.
def create_accounts_table(accounts):
    try:
        # read all available fields.
        fields = read_json(SETTINGS_FOLDER + "account.json")
        with dpg.table(tag=TAG_ACCOUNTS_TABLE, label=TAG_ACCOUNTS_TABLE):

            fieldsNames = tuple(fields.keys())
            # Add columns
            for field in fieldsNames:
                dpg.add_table_column(label=field)

            for account in accounts:
                add_account(account, fields)
    except:
        dpg.add_text("Problem whle table creation.")

# Method to add accounts.
def add_account(account, fields):
    # Add values.
    with dpg.table_row():
        for field in fields.keys():
            value = "~" # it means that it's empty.
            secret = False

            if (account.contains_field(field)):
                value = account.get(field)
            
            if (fields[field] == "secret"):
                secret = True

            dpg.add_input_text(default_value=value, width=-1, password=secret)
