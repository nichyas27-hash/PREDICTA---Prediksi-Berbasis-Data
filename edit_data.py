import streamlit as st
from components.readFile import readFile
from pages_content.edit_data.cleaning_data import clean_data

def app():

    with st.container(key="box-uploader"):
        df = readFile()

        if df is not None:
            st.session_state["df"] = df

    with st.container(key="box-table"):
        if "df" in st.session_state:
            st.data_editor(
                data=st.session_state["df"],
                num_rows="dynamic",
                hide_index=True,
                use_container_width=True
            )

    with st.container(key="box-cleaning"):
        if "df" in st.session_state:
            clean_data(st.session_state["df"])
