import pandas as pd
import streamlit as st
from pmdarima import auto_arima
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from prophet import Prophet
from components.echarts import demo_line, prophet_line_demo

@st.cache_data
def load_data():
    return pd.read_csv('assets/data/demo.csv', encoding='utf-8')


@st.cache_resource
def train_prophet(df_prophet):
    model = Prophet()
    model.fit(df_prophet)
    return model


@st.cache_resource
def train_arima(data):
    model = auto_arima(
        data,
        seasonal=False,
        trace=True,
        suppress_warnings=True
    )
    return model


@st.cache_resource
def train_des(data, trend, seasonal=None, seasonal_periods=None):
    model = ExponentialSmoothing(
        endog=data,
        trend=trend,
        seasonal=seasonal,
        seasonal_periods=seasonal_periods
    )
    return model.fit()


def demo():

    with st.container(key="data"):
        df = load_data()

    # ================= PROPHET =================
    with st.container(key="demo_Prophet"):

        with st.container(key="input_prophet"):
            n = st.number_input("Periode(n) : ", value=10, min_value=1, step=1, key="n1")

        with st.container(key="run_Prophet"):

            df_prophet = pd.DataFrame({
                "ds": df["Waktu"],
                "y": df["Aktual"]
            })

            model = train_prophet(df_prophet)

            f = model.make_future_dataframe(periods=n, freq='MS')
            Ft = model.predict(f)

            result = pd.DataFrame({
                "Waktu": Ft['ds'],
                "Forecast": Ft["yhat"],
                "Batas Bawah": Ft["yhat_lower"],
                "Batas Atas": Ft["yhat_upper"]
            })

            prophet_line_demo(result)

        b1, b2 = st.columns(2)

        with b1:
            st.badge("Metode Prophet", color='primary')

        with b2:
            st.badge("Prophet Method by Meta", color='green')


    # ================= MOVING AVERAGE =================
    col1, col2 = st.columns(2)

    with col1:

        with st.container(key="demo_MA"):

            n = st.number_input("Periode (n): ", value=3, min_value=1, step=1, key="n2")

            df[f'MA({n})'] = df['Aktual'].rolling(window=n).mean()

            df_histMA = pd.DataFrame({
                "Waktu": df["Waktu"],
                "Aktual": df["Aktual"],
                f"MA({n})": df[f"MA({n})"],
                "Forecast": df[f"MA({n})"].shift(1)
            })

            df_forecastMA = pd.DataFrame({
                "Waktu": ["T1"],
                "Aktual": [None],
                f"MA({n})": [None],
                "Forecast": df[f"MA({n})"].iloc[-1]
            })

            result = pd.concat([df_histMA, df_forecastMA], ignore_index=True)

            result = result.fillna('None')

            demo_line(result)

        b3, b4 = st.columns(2)

        with b3:
            st.badge("Rata-Rata Bergerak", color='primary')

        with b4:
            st.badge("Moving Average", color='green')


    # ================= DES =================
    with col2:

        with st.container(key="demo_DES"):

            with st.container(key="input_DES"):

                i1, i2 = st.columns(2)

                with i1:
                    n = st.number_input("Periode(n): ", value=10, min_value=1, step=1, key="n3")

                with i2:
                    type = st.selectbox(
                        label="Type",
                        options=['Aditif', 'Multiplikatif'],
                        key="type1"
                    )

            with st.container(key="run_DES"):

                if type == 'Aditif':

                    fit = train_des(df['Aktual'], 'add')

                else:

                    fit = train_des(df['Aktual'], 'mul')

                Ft = fit.forecast(n)

                df_histDES = pd.DataFrame({
                    'Waktu': df['Waktu'],
                    'Aktual': df['Aktual'],
                    'Forecast': [None]*len(df)
                })

                df_forecastDES = pd.DataFrame({
                    'Waktu': [f"T{i+1}" for i in range(n)],
                    'Aktual': [None]*n,
                    'Forecast': Ft
                })

                result = pd.concat([df_histDES, df_forecastDES], ignore_index=True)

                demo_line(result)

        b5, b6 = st.columns(2)

        with b5:
            st.badge("Penghalusan Ekponensial Holt", color='primary')

        with b6:
            st.badge("Holt-Smooting")


    # ================= TES =================
    col3, col4 = st.columns(2)

    with col3:

        with st.container(key="demo_TES"):

            with st.container(key="input_TES"):

                i3, i4, i5 = st.columns(3)

                with i3:
                    n = st.number_input("Periode(n): ", value=10, min_value=1, step=1, key="n4")

                with i4:
                    s = st.number_input("Periode(s): ", value=4, min_value=2, step=1, key="s1")

                with i5:
                    type = st.selectbox(
                        label="Type",
                        options=['Aditif', 'Multiplikatif'],
                        key="type2"
                    )

            with st.container(key="run_TES"):

                if type == 'Aditif':

                    fit = train_des(df['Aktual'], 'add', 'add', s)

                else:

                    fit = train_des(df['Aktual'], 'mul', 'mul', s)

                Ft = fit.forecast(n)

                df_histTES = pd.DataFrame({
                    'Waktu': df['Waktu'],
                    'Aktual': df['Aktual'],
                    'Forecast': [None]*len(df)
                })

                df_forecastTES = pd.DataFrame({
                    'Waktu': [f"T{i+1}" for i in range(n)],
                    'Aktual': [None]*n,
                    'Forecast': Ft
                })

                result = pd.concat([df_histTES, df_forecastTES], ignore_index=True)

                demo_line(result)

        b7, b8 = st.columns(2)

        with b7:
            st.badge("Penghalusan Ekponensial Holt-Winters", color='primary')

        with b8:
            st.badge("Holt-Winters Smooting")

    # ================= ARIMA =================
    with col4:

        with st.container(key="demo_ARIMA"):

            with st.container(key="input_ARIMA"):

                n = st.number_input("Periode(n) : ", value=10, min_value=1, step=1, key="n5")

            with st.container(key="run_ARIMA"):

                model = train_arima(df['Aktual'])

                Ft = model.predict(int(n))

                df_histAR = pd.DataFrame({
                    'Waktu': df['Waktu'],
                    'Aktual': df['Aktual'],
                    'Forecast': [None]*len(df)
                })

                df_forecastAR = pd.DataFrame({
                    'Waktu': [f"T{i+1}" for i in range(n)],
                    'Aktual': [None]*n,
                    'Forecast': Ft
                })

                result = pd.concat([df_histAR, df_forecastAR], ignore_index=True)

                demo_line(result)

        b9, b10 = st.columns(2)

        with b9:
            st.badge("Metode ARIMA", color='primary')

        with b10:
            st.badge("ARIMA(p,d,q)")