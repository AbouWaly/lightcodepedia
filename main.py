import sys
import streamlit as st

from lightcode import page_config, import_module, about

page_config(__file__)

if sys.flags.optimize > 0:
    raise RuntimeError("LightCode requires asserts to be active. Please run without -O.")

def module_page(sel_file: str):
    import_module(sel_file)

def welcome_page(sel_file: str):
    on_design = False

    import_module(sel_file, on_design)


st.session_state.mud = ""

about()

welcome_page("welcome")