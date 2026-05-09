import streamlit as st
from components.readFile import readFile
from streamlit_option_menu import option_menu
from pages_content.visualization.line_generate import line_visualization
from pages_content.visualization.bar_generate import bar_visualization
from pages_content.visualization.pie_generate import pie_visualization
from pages_content.visualization.radar_generate import radar_visualization

def app():
    with st.container(key="box1"):
        df = readFile()

    with st.container(key="box2"):
        try:
            st.write(df)
            st.session_state["df"] = df
        except:
            st.warning("Data belum diupload")

    selected = option_menu(
        menu_title=None,
        menu_icon=None,
        default_index=0,
        options=['Line-Chart', 'Bar-Chart', 'Pie-Chart', 'Radar-Chart'],
        icons=['graph-up', 'bar-chart', 'pie-chart', 'radar'],
        orientation='horizontal'
    )

    if selected == 'Line-Chart':
        try: 
            line_visualization(df)
        except:
            ""

    elif selected == 'Bar-Chart':
        try:
            bar_visualization(df)
        except:
            ""
    
    elif selected == 'Pie-Chart':
        try:
            pie_visualization(df)
        except:
            ""

    elif selected == 'Radar-Chart':
        try:
            radar_visualization(df)
        except:
            ""