import pandas as pd
import streamlit as st
from components.echarts import pie_chart, donut_chart

def pie_visualization(df):
    with st.container(key="box-1"):
        col1, col2, col3 = st.columns(3)
        with col1:
            kategory = st.selectbox(
                label="Pilih kolom kategori: ",
                options=df.columns,
                index=0,
                key="isKategory"
            )

        with col2:
            data = st.selectbox(
                label="Pilih kolom data: ",
                options=df.columns,
                index=1,
                key="isData"
                )

        with col3:    
            label = st.text_input("Tambah label grafik: ", value=None, key="label1")

    with st.container(key="model-pie"):
        pie_chart(
            df=df,
            kategory=kategory,
            data=data,
            label=label,
        )

        if "add_series" not in st.session_state:
            st.session_state.add_series = False

    with st.container(key="box-button"):
        if st.button(
            label="beralih ke donut-chart",
            icon="🍩",
            type="tertiary"):
            
            st.session_state.add_series = True

    with st.container(key="box-2"):
        with st.container(key="model-donut"):
            donut_chart(
                df=df,
                data=data,
                kategory=kategory,
                label=label
            )