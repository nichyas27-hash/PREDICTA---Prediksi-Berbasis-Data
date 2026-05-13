import pandas as pd
import streamlit as st

def clean_data(df):
    selected = st.menu_button(
        label="Clean Data",
        options=["Remove Duplicates", "Drop NA Values", "Fill Missing Values", "Remove Outliers"],
        icon="🧹"
    )

    if selected == "Remove Duplicates":
        try:
            with st.form("remove_duplicates_form"):
                col1, col2 = st.columns(2)
                with col1:
                    data = st.selectbox(
                        label="Pilih Kolom Dupikat",
                        options=df.columns
                    )
                with col2:
                    apply = st.form_submit_button("Terapkan", key="remove_duplicate")
    
                if apply:
                    df = df.drop_duplicates(subset=[data]) 
                    st.success("Duplicates removed successfully! :3")
                    st.session_state["df"] = df
                    st.rerun()

        except Exception as e:
            st.error(f"Error removing duplicates: {e}")
    
    elif selected == "Drop NA Values":
        try:
            with st.form("drop_na_form"):
                col1, col2 = st.columns(2)
                with col1:
                    data = st.selectbox(
                            label="Pilih Kolom NA",
                            options=df.columns
                        )
                with col2:
                    apply = st.form_submit_button("Terapkan", key="drop_na")
    
                if apply:
                    df = df.dropna(subset=[data])
                    st.success("Null values dropped successfully! :3")
                    st.session_state["df"] = df
                    st.rerun()
                
        except Exception as e:
            st.error(f"Error dropping na values: {e}")
    
    elif selected == "Fill Missing Values":
        try:
            with st.form("fill_na_form"):
                col1, col2, col3 = st.columns(3)
    
                with col1:
                    data = st.selectbox(
                        "Pilih Kolom Value",
                        options=df.columns
                    )
    
                with col2:
                    fill = st.text_input("Masukkan value di sini:")
    
                with col3:
                    apply = st.form_submit_button("Terapkan", key="fill_na")
    
                if apply:
                    df[data] = df[data].fillna(fill)
                    st.success("Missing values filled successfully!")
                    st.session_state["df"] = df
                    st.rerun()

        except Exception as e:
            st.error(f"Error filling missing values: {e}")
    
    elif selected == "Remove Outliers":
        try:
            with st.form("remove_outlier_form"):
                col1, col2 = st.columns(2)
                with col1:
                    data = st.selectbox(
                        label="Pilih Kolom Outlier",
                        options=df.columns
                    )
                with col2:
                    apply = st.form_submit_button("Terapkan", key="remove_outliers")
    
                if apply:
                    q1 = df[data].quantile(0.25)
                    q3 = df[data].quantile(0.75)
                    iqr = q3 - q1
                    lower_bound = q1 - 1.5 * iqr
                    upper_bound = q3 + 1.5 * iqr
                    df = df[(df[data] >= lower_bound) & (df[data] <= upper_bound)]
                    st.success("Outliers removed successfully! :3")
                    st.session_state["df"] = df
                    st.rerun()

        except Exception as e:
            st.error(f"Error removing outliers: {e}")
