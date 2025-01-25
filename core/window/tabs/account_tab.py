import dearpygui.dearpygui as dpg
from ...shared.utils import import_accounts, read_json
from ...shared.constants import SETTINGS_FOLDER
from ...logic.account import Account

TAG_ACCOUNTS = "Accounts"
TAG_ACCOUNTS_TABLE = "Accounts_Table"
TAG_ACCOUNTS_ADD = "Accounts_Add"
TAG_ACCOUNTS_REFRESH = "Accounts_Refresh"
TAG_ACCOUNTS_SAVE = "Accounts_Save"
TAG_ACCOUNT_FORM = "Accounts_Form"

# Create accounts tabs with tree view.
def create_accounts_tab():
    with dpg.tab(label="Accounts", tag=TAG_ACCOUNTS):
        dpg.add_spacer()
        
        # Horizontal group.
        with dpg.group(horizontal=True):
            dpg.add_text("Accounts")
            dpg.add_button(label= "+", tag=TAG_ACCOUNTS_ADD, callback=create_account)
            dpg.add_button(label="refresh", tag=TAG_ACCOUNTS_REFRESH, callback=refresh_table)
            dpg.add_button(label="save", tag=TAG_ACCOUNTS_SAVE)
        dpg.add_separator()

        # Add table.
        refresh_table()

# Create accounts table.
def create_accounts_table(accounts):
    try:
        # read all available fields.
        fields = read_json(SETTINGS_FOLDER + "account.json")
        with dpg.table(tag=TAG_ACCOUNTS_TABLE, label=TAG_ACCOUNTS_TABLE, parent=TAG_ACCOUNTS):

            fieldsNames = tuple(fields.keys())
            # Add columns
            for field in fieldsNames:
                dpg.add_table_column(label=field)

            for account in accounts:
                add_account(account, fields)
    except:
        print("Problem whle table creation.")

# Method to add accounts.
def add_account(account, fields):
    # Add values.
    with dpg.table_row(parent=TAG_ACCOUNTS_TABLE):
        for field in fields.keys():
            value = "~" # it means that it's empty.
            secret = False

            if (account.contains_field(field)):
                value = account.get(field)
            
            if (fields[field] == "secret"):
                secret = True

            tag = account.get('filename') + field
            input_field = dpg.add_input_text(default_value=value, width=-1, password=secret, tag=tag, readonly=True)
            with dpg.popup(input_field, mousebutton=dpg.mvMouseButton_Right, ):
                # Add menu options to the context menu
                # TODO: fix strange behaviour with positioning.
                dpg.add_menu_item(label="Edit", user_data=input_field, callback=edit_value)
                dpg.add_menu_item(label="Copy", user_data=tag, callback=copy_value)

def copy_value(sender, _, user_data):
    value = dpg.get_value(user_data)
    dpg.set_clipboard_text(value)

def edit_value(_, __, user_data):
    print(user_data)

def create_account():
    try:
        fields = read_json(SETTINGS_FOLDER + "account.json")

        with dpg.window(label="Account creation", modal=True, tag=TAG_ACCOUNT_FORM, show=True, autosize=True, on_close=lambda: dpg.delete_item(TAG_ACCOUNT_FORM)):
            for field in fields.keys():
                dpg.add_input_text(label=field, tag=field_to_tag(field))

            with dpg.group(horizontal=True):
                dpg.add_button(label="Add", callback=save_account)
    except:
        print("Problem in creation of form.")

def field_to_tag(field):
    return "tag_" + field + "_form"

def save_account():
    fields = read_json(SETTINGS_FOLDER + "account.json")
    accountData = {}

    # collect data from modal.
    for field in fields.keys():
        try:
            value = dpg.get_value(field_to_tag(field))
        except:
            accountData[field] = ''   
        else:
            accountData[field] = value

    
    # create account
    name = accountData.get("name", "noName")
    accountData['filename'] = name + '.json'
    # add account
    account = Account(name, accountData)
    account.save()
    add_account(account, fields)
    
    # close form
    dpg.delete_item(TAG_ACCOUNT_FORM)
    
def refresh_table():
    try:
        if dpg.does_item_exist(TAG_ACCOUNTS_TABLE):
            dpg.delete_item(TAG_ACCOUNTS_TABLE)
        accounts = import_accounts()
    except Exception as e:
        dpg.add_text("No accounts")
    else:
        create_accounts_table(accounts)