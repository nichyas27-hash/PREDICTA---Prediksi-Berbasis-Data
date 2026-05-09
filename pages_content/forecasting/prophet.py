import pandas as pd
import streamlit as st
from prophet import Prophet
from components.echarts import prophet_line_forecast

def prophet(df):
    with st.container(key="input_prophet"):
        n = st.number_input("Ketik periode(n) forecast prophet: ", min_value=1, step=1)
    
    with st.container(key="Prophet"):
        with st.spinner("Membangun model Prophet..."):
            try: 
                df = pd.DataFrame({
                    "ds": df["Waktu"],
                    "y": df["Aktual"]
                })
                model = Prophet()
                model.fit(df)

                f = model.make_future_dataframe(periods=n, freq='MS')
                Ft = model.predict(f)

                result = pd.DataFrame({
                    "Waktu": Ft['ds'], 
                    "Forecast": Ft["yhat"],
                    "Batas Bawah": Ft["yhat_lower"],
                    "Batas Atas": Ft["yhat_upper"]
                })

                st.write(result)
                prophet_line_forecast(result)

            except:
                st.warning("Jenis data tidak dapat digunakan model Prophet")