import dearpygui.dearpygui as dpg

TAG_MAIN_MENU = "Main"

def create_main_menu():
    with dpg.window(tag=TAG_MAIN_MENU):
        with dpg.menu_bar():
            with dpg.menu(label="Settings"):
                dpg.add_menu_item(label="About", callback=show_popup)
                dpg.add_menu_item(label="Account settings", callback=show_popup)

def show_popup():
    print("click")
