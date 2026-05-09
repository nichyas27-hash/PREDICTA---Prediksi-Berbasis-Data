import pandas as pd
import streamlit as st
from pages_content.home.demo import demo

def app():
    with st.container(key="box-header"):
        st.markdown("""<h3>Welcome to PREDICTA</h3>
                    <p><b>PREDICTA: Prediksi Berbasis Data</b>, <q><I>solusi pintar prediksi berbasis data</I></q>. PREDICTA hadir membantumu dalam memecahkan masalah peramalan,
                    segera upload datamu dan dapatkan insight baru! </p>""", unsafe_allow_html=True)
    
    with st.container(key="box-body"):
        st.markdown("""<h4>DEMONSTRASI</h4>
                    <p>Demontrasi di bawah ini menggunakan data dummy dengan 4 metode peramalan yang berbeda, yaitu:
                    Moving Averange, Exponential Smoothing, ARIMA, dan Prophet by Meta</p>""", unsafe_allow_html=True)
        df = pd.read_csv('assets/data/demo.csv')
        st.write(df)
        st.link_button("mulai ramalkan dengan datamu sendiri", url='edit_data.py', icon='📂')
        
    with st.container(key="box-demo_content"):
        demo()