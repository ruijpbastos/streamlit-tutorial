import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.header("st.write")

st.write("Hello, *World!* :sunglasses:")

st.write(1234)

df = pd.DataFrame({"col01": [1, 2, 3, 4], "col02": [10, 20, 30, 40]})
st.write(df)

st.write("Below is a DataFrame:", df, "Above is a DataFrame.")

fig = plt.figure()
df2 = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])
c = plt.scatter(df2["a"], df2["b"], c=df2["c"], figure=fig)
st.write(fig)
