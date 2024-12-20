import streamlit as st

'Hello World!'

''' 
# This is my first app
This is a _example code_.
'''

import pandas as pd

df = pd.DataFrame({'col1': [1,2,3], 'col2': [4,5,6]})
df

x = 10
x

import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
fig