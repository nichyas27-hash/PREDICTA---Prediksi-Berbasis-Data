import pandas as pd
import streamlit as st
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from components.echarts import forecast_line

def SES(df):
    with st.container(key="input_SES"):
        n = st.number_input("Ketik periode(n) forecast eksponensial smoothing: ", min_value=1, step=1)
    
    with st.container(key="SES"):
        with st.spinner("Membangun model Single Exponential Smoothing..."):
            try: 
                model = ExponentialSmoothing(
                    endog=df['Aktual'],
                    trend=None,
                    seasonal=None,
                )
                fit = model.fit()
                Ft = fit.forecast(n)

                df_hist = pd.DataFrame({
                    "Waktu": df["Waktu"],
                    "Aktual": df["Aktual"],
                    "Forecast": [None]*len(df)
                })

                df_forecast = pd.DataFrame({
                    "Waktu": [f"F{i+1}" for i in range(n)],
                    "Aktual": [None]*n,
                    "Forecast": Ft
                })

                result = pd.concat([df_hist, df_forecast], ignore_index=True)
                st.write(result)
                forecast_line(result)

            except:
                st.warning("Jenis data tidak dapat digunakan model Single Smoothing")

def DES(df):
    with st.container(key="input_DES"):
        col1, col2 = st.columns(2)
        with col1: 
            n = st.number_input("Ketik periode(n) forecast eksponensial smoothing: ", min_value=1, step=1)
        with col2:    
            type = st.selectbox(
                label="Pilih type holt smoothing",
                options=['Aditif', 'Multiplikatif']
            )
    
    with st.container(key="DES"):
        if type == 'Aditif': 
            with st.spinner("Membangun model aditif Holt Smoothing..."):
                try: 
                    model = ExponentialSmoothing(
                        endog=df['Aktual'],
                        trend='add',
                        seasonal=None,
                    )  
                    fit = model.fit()
                    Ft = fit.forecast(n)

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
                    st.warning("Jenis data tidak dapat digunakan model aditif Holt Smoothing")
        
        elif type == 'Multiplikatif':
            with st.spinner("Membangun model multiplikatif Holt Smoothing..."): 
                try: 
                    model = ExponentialSmoothing(
                        endog=df['Aktual'],
                        trend='mul',
                        seasonal=None,
                    )  
                    fit = model.fit()
                    Ft = fit.forecast(n)

                    df_hist = pd.DataFrame({
                        'Waktu': df['Waktu'],
                        'Aktual': df['Aktual'],
                        'Forecast': [None]*len(df)
                    })

                    df_forecast = pd.DataFrame({
                        'Waktu': [f"T{i+1}" for i in range(n)],
                        'Aktual': [None]*n,
                        'Forecast': Ft
                    })

                    result = pd.concat([df_hist, df_forecast], ignore_index=True)
                    st.write(result)
                    forecast_line(result)
                
                except: 
                    st.warning("Jenis data tidak dapat digunakan model multiplikatif Holt Smoothing")

def TES(df):
    with st.container(key="input_TES"):
        col1, col2 = st.columns(2)
        with col1: 
            n = st.number_input("Ketik periode(n) forecast eksponensial smoothing: ", min_value=1, step=1)
        with col2: 
            s = st.number_input("Ketik periode(s) musim eksponensial smoothing: ", min_value=2, step=1)
        type = st.selectbox(
            label="Pilih type holt smoothing",
            options=['Aditif', 'Multiplikatif']
        )

    with st.container(key="TES"):
        if type == 'Aditif':
            with st.spinner("Membangun model aditif Holt-Winters Smoothing..."):
                try:  
                    model = ExponentialSmoothing(
                        endog=df['Aktual'],
                        trend='add',
                        seasonal='add',
                        seasonal_periods=s
                    )  
                    fit = model.fit()
                    Ft = fit.forecast(n)

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
                    st.warning("Jenis data tidak dapat digunakan model aditif Holt-Winters Smoothing")

        elif type == 'Multiplikatif': 
            with st.spinner("Membangun model multiplikatif Holt-Winters Smoothing..."):
                try:
                    model = ExponentialSmoothing(
                        endog=df['Aktual'],
                        trend='mul',
                        seasonal='mul',
                        seasonal_periods=int(s)
                    )  
                    fit = model.fit()
                    Ft = fit.forecast(n)

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
                    st.warning("Jenis data tidak dapat digunakan model multiplikatif Holt-Winters Smoothing ")

