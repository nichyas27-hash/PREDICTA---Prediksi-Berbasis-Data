import numpy as np
import streamlit as st

def columns_error(df):

    df['Error'] = df['Aktual'] - df['Forecast']
    df['Error Absolut'] = np.abs(df['Error'])
    df['Error Relatif'] = df['Error Absolut'] / df['Aktual'] * 100

    result = df[['Waktu', 'Aktual', 'Forecast',
                 'Error', 'Error Absolut', 'Error Relatif']]

    st.write(result)

    return result