import dearpygui.dearpygui as dpg

from .menu.main_menu import create_main_menu, TAG_MAIN_MENU
from .menu.tabs_menu import create_tabs

def start():
    dpg.create_context()

    create_main_menu()
    create_tabs()

    dpg.create_viewport(title='AntiSibil', width=600, height=400)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window(TAG_MAIN_MENU, True)
    dpg.start_dearpygui()
    dpg.destroy_context()