import streamlit as st
import streamlit_antd_components as sac
import home
import forecasting
import edit_data
import visualization
import error_calculation

st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
""", unsafe_allow_html=True)

st.set_page_config("PREDICTA", page_icon='bar-chart', layout='wide')
with open("css/main.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""
<div class="topbar">
    <div class="topbar-title">PREDICTA: Prediksi Berbasis Data</div>
    <div class="topbar-midle">
        <form action="https://www.google.com/search" method="get" target="_blank">
            <input 
                type="text"
                name="q"
                placeholder="Cari di Google..."
                class="searchbox"
            >
        </form>
    </div>
    <div class="topbar-right">
            <a href="https://github.com/nichyas27-hash" target="_blank"><i class="fab fa-github"></i></a>  
            <a href="https://nichyas27.site" target="_blank"><i class="fas fa-user"></i></a> 
    </div>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.image('assets/icons/Logo.png')
    selected = sac.menu([
        sac.MenuItem('Home', icon='house'),
        sac.MenuItem('Edit Data', icon='table'),
        sac.MenuItem('Forecasting', icon='graph-up',
                     children=[
                          sac.MenuItem('Moving Average', icon='graph-up'),
                          sac.MenuItem('Exponential Smoothing', icon='graph-up'),
                          sac.MenuItem('ARIMA', icon='graph-up'),
                          sac.MenuItem('Prophet', icon='graph-up')
                     ]),
        sac.MenuItem('Visualization', icon='pie-chart'),
        sac.MenuItem('Error Calculation', icon='calculator')
    ], variant='filled')

if selected == 'Home':
    home.app()

elif selected == 'Edit Data':
    edit_data.app()

elif selected in ['Moving Average','Exponential Smoothing','ARIMA','Prophet']:      
    forecasting.app(selected)

elif selected == 'Visualization':
    visualization.app()

elif selected == 'Error Calculation':
    error_calculation.app()

    
    

