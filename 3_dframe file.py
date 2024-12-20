import streamlit as st
import numpy as np
import pandas as pd

'# Display a dataframe as an interactive table.'
dataframe = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.dataframe(dataframe)   

'# Displays a line chart'
st.line_chart(dataframe)

'# Displays the map data'
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)