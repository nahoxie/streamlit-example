import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to the New S&OP Routing Generator!


"""
def main():
    st.title("Grid Layout Example")

    # Define the number of rows and columns in the grid
    num_rows = 3
    num_cols = 3

    # Create a grid layout using columns
    for i in range(num_rows):
        cols = st.columns(num_cols)
        for j in range(num_cols):
            # Display content in each grid cell
            cols[j].write(f"Row {i + 1}, Column {j + 1}")

if __name__ == "__main__":
    main()


num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

st.altair_chart(alt.Chart(df, height=1200, width=1200)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))
