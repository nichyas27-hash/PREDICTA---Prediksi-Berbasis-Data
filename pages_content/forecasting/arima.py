import pandas as pd
import streamlit as st
from pmdarima import auto_arima
from components.echarts import forecast_line

def ARIMA(df):
    with st.container(key="input_ARIMA"):
        n = st.number_input("Ketik periode(n) forecast arima: ", min_value=1, step=1)
        boxcox = st.checkbox("Stabilkan varians (Box-Cox)", value=False)
    
    with st.container(key="ARIMA"):
        with st.spinner("Membangun model ARIMA..."):
            try: 
                model = auto_arima(
                    df['Aktual'],
                    seasonal=False,
                    trace=True,
                    suppress_warnings=True,
                    boxcox=boxcox
                )
                st.write(model)
                Ft = model.predict(int(n))

                df_hist = pd.DataFrame({
                    'Waktu': df['Waktu'],
                    'Aktual': df['Aktual'],
                    'Forecast': [None]*len(df)
                })

                df_forecast = pd.DataFrame({
                    'Waktu': [f"F{i+1}" for i in range(n)],
                    'Aktual': [None]*n,
                    'Forecast': Ft
                })

                result = pd.concat([df_hist, df_forecast], ignore_index=True)
                st.write(result)
                forecast_line(result)

            except: 
                st.warning("Jenis data tidak dapat digunakan model ARIMA(p,d,q)")

def SARIMA(df):
    with st.container(key="input_SARIMA"):
        col1, col2 = st.columns(2)
        with col1: 
            n = st.number_input("Ketik periode(n) forecast arima: ", min_value=1, step=1)
            boxcox = st.checkbox("Stabilkan varians (Box-Cox)", value=False) 
        with col2: 
            s = st.number_input("Ketik periode(s) musim arima: ", min_value=2, step=1)  
    
    with st.container(key="SARIMA"):
        with st.spinner("Membangun model SARIMA..."):
            try: 
                model = auto_arima(
                    df['Aktual'],
                    seasonal=True,
                    m=s,
                    trace=True,
                    suppress_warnings=True,
                    boxcox=boxcox
                )
                st.write(model)
                Ft = model.predict(n)

                df_hist = pd.DataFrame({
                    'Waktu': df['Waktu'],
                    'Aktual': df['Aktual'],
                    'Forecast': [None]*len(df)
                })

                df_forecast = pd.DataFrame({
                    'Waktu': [f"F{i+1}" for i in range(n)],
                    'Aktual': [None]*n,
                    'Forecast': Ft
                })

                result = pd.concat([df_hist, df_forecast], ignore_index=True)
                st.write(result)
                forecast_line(result)

            except:
                st.warning("Jenis data tidak dapat digunakan model SARIMA(p,d,q)(P,D,Q)s")
