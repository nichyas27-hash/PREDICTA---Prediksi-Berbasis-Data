import pandas as pd
import streamlit as st

def readFile():
    file = st.file_uploader(
        label="Upload datamu di sini..",
            help="Insert your data here and only one file extension is allowed (csv or .csv)",
            type= 'csv',
        )
    if file is not None:
        file = pd.read_csv(file)
        return file

    return None
    
def dataTest(df):
    try:
        col1, col2 = st.columns(2)
        with col1:
            t = st.selectbox(
                label="Pilih kolom waktu",
                options=df.columns,
                index=0            
            )

        with col2:
            xt = st.selectbox(
                label="Pilih kolom data aktual",
                options=df.columns,
                index=1
            )
        
        data = pd.DataFrame({'Waktu': df[t], 'Aktual': df[xt]})
        st.write(data)
        return data
    
    except:
        st.warning("Data belum diupload :3")

def isTime(df):
    time = st.selectbox(
        label="Pilih kolom waktu: ",
        options=df.columns,
        index=0,
    )
    return time
