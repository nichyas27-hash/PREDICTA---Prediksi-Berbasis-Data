import streamlit as st
from components.readFile import readFile
from pages_content.edit_data.cleaning_data import clean_data

def app():
    st.info("Fitur Clean Data maaih belum bisa digunakan, karena aku lagi sibuk KP jadi nanti² aja aku lanjutin : 3")

    with st.container(key="box-uploader"):
        df = readFile()

        if df is not None and "df" not in st.session_state:
            st.session_state["df"] = df

    with st.container(key="box-cleaning"):
        if "df" in st.session_state:
            clean_data()
            
    with st.container(key="box-table"):
        if "df" in st.session_state:
            edited_df = st.data_editor(
                data=st.session_state["df"],
                num_rows="dynamic",
                hide_index=True,
                use_container_width=True
            )
            st.session_state["df"] = edited_df


