import pandas as pd
import streamlit as st
from components.echarts import bar_chart

def bar_visualization(df):
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
            data_1 = st.selectbox(
                label="Pilih kolom data: ",
                options=df.columns,
                index=1,
                key="isData"
                )

        with col3:    
            label_1 = st.text_input("Tambah label grafik: ", value=None, key="label1")

    with st.container(key="model-bar1"):
        bar_chart(
            df=df,
            kategory=kategory,
            data_1=data_1,
            data_2=None,
            label_1=label_1,
            label_2=None
        )

        if "add_series" not in st.session_state:
            st.session_state.add_series = False

    with st.container(key="box-button"):
        if st.button(
            label="tambahkan bar-chart",
            icon="📊",
            type="tertiary"):
            
            st.session_state.add_series = True

    with st.container(key="box-2"):
        if st.session_state.add_series:
            col1, col2 = st.columns(2)

            with col1:
                data_2 = st.selectbox(
                    label="Pilih kolom data:",
                    options=df.columns,
                    index=1,
                    key="isFt"
                )

            with col2:
                label_2 = st.text_input(
                    "Tambah label grafik:",
                    key="label2"
                )

        with st.container(key="model-bar2"):
            bar_chart(
                df=df,
                kategory=kategory,
                data_1=data_1,
                data_2=data_2,
                label_1=label_1,
                label_2=label_2
            )