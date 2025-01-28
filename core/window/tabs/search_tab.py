import dearpygui.dearpygui as dpg
from ...logic.parsing.testparser import gmgn_sol
import asyncio

TAG_ANALYTIC_SEARCH_TAB = "Search"
def create_search_tab():
    with dpg.tab(tag=TAG_ANALYTIC_SEARCH_TAB, label="Search"):
        with dpg.group(horizontal=True):
            input = dpg.add_input_text()
            # we pass input in user_data to track id and get value
            dpg.add_button(label="Analyze", callback=search_button_callback, user_data=input)

def search_button_callback(_, __, input_id):
    asyncio.run(search_token_info(input_id))

async def search_token_info(input_id):
    token_id = dpg.get_value(input_id).strip()

    if (token_id == ""):
        return
    
    r = await gmgn_sol(token_id)
    
    dpg.add_text(r, parent=TAG_ANALYTIC_SEARCH_TAB)
    

