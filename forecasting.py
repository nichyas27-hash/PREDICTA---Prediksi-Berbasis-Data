import streamlit as st
from streamlit_option_menu import option_menu
from pages_content.forecasting.movingAverage import MA
from pages_content.forecasting.exponentialSmoothing import SES, DES, TES
from pages_content.forecasting.arima import ARIMA, SARIMA
from pages_content.forecasting.prophet import prophet
from components.readFile import readFile, dataTest

def app(method):
    with st.container(key="box1"):
        file = readFile()

    with st.container(key="box2"):
        df = dataTest(file)

    with st.container(key="box3"):
        if method == 'Moving Average':
            MA(df)

        elif method == 'Exponential Smoothing':
            model = option_menu(
                menu_title=None,
                menu_icon=None,
                options=['Single Exponential Smoothing (SES)', 'Holt Smoothing (Double)', 'Holt-Winters Smoothing (Triple)'],
                icons=['graph-up','graph-up','graph-up'],
                orientation='horizontal',
            )
            if model == 'Single Exponential Smoothing (SES)':
                SES(df)
            elif model == 'Holt Smoothing (Double)':
                DES(df)
            elif model == 'Holt-Winters Smoothing (Triple)':
                TES(df)

        elif method == 'ARIMA':
            model = option_menu(
                menu_title=None,
                menu_icon=None,
                options=['ARIMA(p,d,q)', 'SARIMA(p,d,q)(P,D,Q)s'],
                icons=['graph-up', 'graph-up'],
                orientation='horizontal'
            )
            if model == 'ARIMA(p,d,q)':
                ARIMA(df)
            elif model == 'SARIMA(p,d,q)(P,D,Q)s':
                SARIMA(df)

        elif method == 'Prophet': 
            prophet(df)