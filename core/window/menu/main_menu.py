import dearpygui.dearpygui as dpg
import os, json, glob
from ...shared.utils import read_json
from ...shared.constants import SETTINGS_FOLDER, ACCOUNTS_FOLDER
from ..tabs.account_tab import refresh_table

TAG_MAIN_MENU = "Main"
TAG_SETTINGS_ACCOUNT = "Settings_Account"
TAG_SETTINGS_TABLE = "Settings_Table"
def create_main_menu():
    with dpg.window(tag=TAG_MAIN_MENU):
        with dpg.menu_bar():
            with dpg.menu(label="Settings"):
                dpg.add_menu_item(label="About", callback=show_popup)
                dpg.add_menu_item(label="Account settings", callback=create_account_settings)

def show_popup():
    print("click")

def create_account_settings():
    fields = read_json(SETTINGS_FOLDER + "account.json")

    with dpg.window(label="Account settings", modal=True, tag=TAG_SETTINGS_ACCOUNT, autosize=True,show=True, on_close=lambda: dpg.delete_item(TAG_SETTINGS_ACCOUNT)):
        with dpg.table(label="Account settings", tag=TAG_SETTINGS_TABLE):
            dpg.add_table_column(label="Key")
            dpg.add_table_column(label="Secret")
            dpg.add_table_column(label="Readonly")

            for field in fields.keys():
                with dpg.table_row():
                    dpg.add_input_text(tag=field, width=-1, default_value=field)
                    dpg.add_combo([True, False], tag=field+"_secret", default_value=fields[field]['secret'])
                    dpg.add_combo([True, False], tag=field+"_readonly", default_value=fields[field]['readonly'])

        with dpg.group(horizontal=True):
            dpg.add_button(label="Save", callback=save_settings_option)
            dpg.add_button(label="Add", callback=lambda: add_settings_option(fields))
        
        dpg.add_text("NOTE: It will add new values to your account \nand will override current configuration.")


def add_settings_option(fields):
    option = 'option'+ str(len(fields.keys()))
    fields[option] = {
        "secret" : False,
        "readonly" : False
    }

    with dpg.table_row(parent=TAG_SETTINGS_TABLE):
        dpg.add_input_text(tag=option, width=-1, default_value='')
        dpg.add_combo([True, False], tag=option, default_value=False)
        dpg.add_combo([True, False], tag=option, default_value=False)

# Save function, now:
# 0 - it's a key
# 1 - it's a filter
# we can add more save function later.
def save_settings_option():
    account_configuration = {}

    rows_ids = dpg.get_item_children(TAG_SETTINGS_TABLE)[1]
    for rows_id in rows_ids:
        row_items_ids = dpg.get_item_children(rows_id)[1]

        key = dpg.get_value(row_items_ids[0])
        secret = dpg.get_value(row_items_ids[1]) == "True"
        readonly = dpg.get_value(row_items_ids[2]) == "True"

        account_configuration[key] = {
            'secret' : secret,
            'readonly' : readonly
        }

    # we override current account.json
    with open(SETTINGS_FOLDER + "account.json", 'w') as configuration_file:
        json.dump(account_configuration, configuration_file)
        configuration_file.close()

    # we add fields to all accounts 
    for filename in glob.glob(os.path.join(ACCOUNTS_FOLDER, '*.json')):
        with open(filename, 'r+') as account_file:
            account_text = account_file.read()
            account_json = json.loads(account_text)

            for key in account_configuration.keys():
                if (key in account_json.keys()):
                    continue
                           
                # add new value.
                account_json[key] = ""

            account_file.seek(0)  
            json.dump(account_json, account_file, indent=6)
            account_file.truncate()
        account_file.close()


    # we refresh table to show new data
    refresh_table()
        