import streamlit as st
from streamlit.commands.page_config import Layout
from streamlit_extras.app_logo import add_logo
from streamlit_navigation_bar import st_navbar
from streamlit_extras.switch_page_button import switch_page
import home
import snakies
import snakeinfo

st.set_page_config(page_title="Snakies", layout="wide", page_icon="🐍"
                  )


def load_nav_bar():
    pages = ["หน้าหลัก", "Snakies","ข้อมูลงูไทย"]
    logo_path = "images/Snakeimage2vector.svg" 
    styles = {
        "nav": {
            "background-color": "#06402B",
            "height": "90px",
        },
        "img": {
            "padding-right": "1px",
        },
        "span": {
            "color": "white",
            "font-size": "16px",
            "padding": "17px",
            "font-weight": "bold",
            "border-radius": "16px",
        },
        "hover": {
            "color": "lightgreen",
            "font-weight": "bold",
            "text-decoration": "underline",
        },
        "active": {
            "color": "green",
            "background-color": "white",
            "font-weight": "bold",
            "padding": "14px",
            "border": "0px solid #06402B",
        }
    }
    options = {
        "show_menu": False,
        "show_sidebar": False,
        "use_padding": True,
    }

    page = st_navbar(
        pages,
        styles=styles,
        logo_path=logo_path,
        options=options,
    )
    return page


# Load navigation bar
selected_page = load_nav_bar()

# Display the selected page
if selected_page == 'หน้าหลัก':
    home.show()
elif selected_page == 'Snakies':
    snakies.show()
elif selected_page == 'ข้อมูลงูไทย':
    snakeinfo.show()
else:
    home.show()  # Default to Home page