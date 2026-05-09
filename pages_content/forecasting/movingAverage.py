import pandas as pd
import streamlit as st
from components.echarts import forecast_line

def MA(df):
    with st.container(key="input_MA"):
        n = st.number_input("Ketik periode (n) Moving Average", min_value=1, step=1)

    with st.container(key="MA"):
        try: 
            with st.spinner("Membangun model Moving Average..."):
                df[f'MA({n})'] = df['Aktual'].rolling(window=n).mean()

                df_hist = pd.DataFrame({
                    "Waktu": df["Waktu"],
                    "Aktual": df["Aktual"],
                    f"MA({n})": df[f"MA({n})"],
                    "Forecast": df[f"MA({n})"].shift(1)
                })

                df_forecast = pd.DataFrame({
                    "Waktu": [f"T1"],
                    "Aktual": [None],
                    f"MA({n})": [None],
                    "Forecast": df[f"MA({n})"].iloc[-1]
                })

                result = pd.concat([df_hist, df_forecast], ignore_index=True)
                result = result.fillna('None')
                st.write(result)
                forecast_line(result)

        except:
            st.warning("Jenis data tidak dapat digunakan model Moving Average")
