import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv("india.csv")

STATES = df['State'].unique().tolist()
STATES.insert(0,"Overall INDIA")

COLS = df.columns.tolist()

st.sidebar.title("GeoSpatial Data Visualization")

selected_state = st.sidebar.selectbox("Select a State", STATES)
primary = st.sidebar.selectbox("Select a Primary Parameters", COLS)
secondary = st.sidebar.selectbox("Select a Secondary Parameters", COLS)

plot= st.sidebar.button("Generate Plot")

if plot:
    if selected_state == "Overall INDIA":
        state_data = df
    else:
        state_data = df[df['State'] == selected_state]

    fig = px.scatter_mapbox(state_data, lat="Latitude", lon="Longitude",hover_name='District ', color=primary, size=secondary, size_max=15, color_continuous_scale=px.colors.cyclical.IceFire, zoom=3, mapbox_style="carto-positron")

    st.plotly_chart(fig)