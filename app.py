import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

@st.cache_data
def load_data():
    return pd.read_csv("india.csv")

df = load_data()

STATES = df['State'].unique().tolist()
STATES.insert(0, "Overall INDIA")

COLS = [col for col in df.columns if col not in ["Latitude", "Longitude", "District", "State"]]

st.sidebar.title("GeoSpatial Data Visualization")

selected_state = st.sidebar.selectbox("Select a State", STATES)
primary = st.sidebar.selectbox("Select a Primary Parameter", COLS)
secondary = st.sidebar.selectbox("Select a Secondary Parameter", COLS)

if st.sidebar.button("Generate Plot"):
    state_data = df if selected_state == "Overall INDIA" else df[df['State'] == selected_state]

    if primary == secondary:
        st.warning("Primary and Secondary parameters must be different!")
    else:
        zoom_level = 3 if selected_state == "Overall INDIA" else 5
        fig = px.scatter_mapbox(
            state_data,
            lat="Latitude",
            lon="Longitude",
            hover_name="District",
            color=primary,
            size=secondary,
            size_max=15,
            color_continuous_scale=px.colors.cyclical.IceFire,
            zoom=zoom_level,
            mapbox_style="open-street-map"
        )
        st.plotly_chart(fig)
