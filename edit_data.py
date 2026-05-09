import pandas as pd
import streamlit as st
from components.readFile import readFile

def app():
    with st.container(key="box-uploader"):
        df = readFile()

    with st.container(key="box-table"):
        st.data_editor(
            data=df, 
            num_rows='dynamic',
            hide_index=True,
            use_container_width=True,
            width='stretch',
        )