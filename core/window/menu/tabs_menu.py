import dearpygui.dearpygui as dpg

from ..tabs.account_tab import create_accounts_tab
from .main_menu import TAG_MAIN_MENU
TAG_PARENT_TABS = "Tabs"

def create_tabs():
    # Создание виджета Notebook
    with dpg.tab_bar(tag=TAG_PARENT_TABS, parent=TAG_MAIN_MENU):
        create_accounts_tab()
        create_projects_tab()
        create_scenarios_tab()
        create_activity_tab()


# Create projects tab
def create_projects_tab():
    with dpg.tab(label="Projects"):
        dpg.add_text("Here will be list of projects")


# Create scenarious tab
def create_scenarios_tab():
    with dpg.tab(label="Scenarios"):
        dpg.add_text("Here will be list of scenarios")

# Create activity tab
def create_activity_tab():
    with dpg.tab(label="Activity"):
        dpg.add_text("Here will be activity")



