import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('india.csv')

list_of_states = list(df['State'].unique())
list_of_states.insert(0,'overall India')

st.sidebar.title('India Data Visualization')

selected_state = st.sidebar.selectbox('Select s State', list_of_states)
primary = st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter',sorted(df.columns[5:]))


plot = st.sidebar.button('Plot Graph')

if plot:

    st.text('Size represent primary parameter')
    st.text('Color represents secondary parameter')
    if selected_state == 'overall India':
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size=primary, color=secondary, size_max=35, zoom=4, mapbox_style="carto-positron",width=1200, height=700, hover_name='District')

        st.plotly_chart(fig, use_container_width=True)

    else:
        state_df = df[df['State'] == selected_state]

        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, size_max=35, zoom=6,
                                mapbox_style="carto-positron", width=1200, height=700, hover_name='District')

        st.plotly_chart(fig, use_container_width=True)

