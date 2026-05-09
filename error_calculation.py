import streamlit as st
from components.readFile import readFile
from pages_content.error_calculation.method_error import mae, mape, mse, rmse
from pages_content.error_calculation.table_error import columns_error


def app():

    with st.container(key="box1"):
        df = readFile()

    if df is None:
        st.warning("Data belum diupload")
        return

    with st.container(key="box2"):
        col1, col2, col3 = st.columns(3)

        with col1:
            time = st.selectbox(
                label="Pilih kolom waktu:",
                options=df.columns,
                index=0,
                key="isTime"
            )

        with col2:
            aktual = st.selectbox(
                label="Pilih kolom data aktual:",
                options=df.columns,
                index=1,
                key="isData"
            )

        with col3:
            forecast = st.selectbox(
                label="Pilih kolom data forecast:",
                options=df.columns,
                index=1,
                key="isFt"
            )

        data = df[[time, aktual, forecast]].copy()
        data.columns = ["Waktu", "Aktual", "Forecast"]

    with st.container(key="box3"):

        columns_error(data)

        col1, col2 = st.columns(2)

        with col1:
            mean = st.menu_button(
                label="Hitung mean error",
                options=['🧮 MAE', '🧮 MAPE', '🧮 MSE', '🧮 RMSE'],
                icon='🧮'
            )

        with col2:

            if mean == '🧮 MAE':
                result = mae(data)
                st.write("Hasil MAE: ")
                st.subheader(result)

            elif mean == '🧮 MAPE':
                result = mape(data)
                st.write("Hasil MAPE: ")
                st.subheader(f"{result} %")

            elif mean == '🧮 MSE':
                result = mse(data)
                st.write("Hasil MSE: ")
                st.subheader(result)

            elif mean == '🧮 RMSE':
                result = rmse(data)
                st.write("Hasil RMSE: ")
                st.subheader(result)