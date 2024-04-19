import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to the New S&OP Routing Generator!


"""
def main():
    st.title("Editable Grid Example")

    # Sample data for the grid
    data = {
        'Name': ['John', 'Alice', 'Bob'],
        'Age': [30, 25, 35],
        'Gender': ['Male', 'Female', 'Male']
    }

    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    # Display the DataFrame as an editable table
    edited_df = st.table(df)

    # Allow users to edit the data
    for i in range(len(df)):
        for col in df.columns:
            # For each cell, create a text input for editing
            new_value = st.text_input(f'Edit {col} for row {i+1}', df.iloc[i][col])
            # Update the DataFrame with the new value
            df.at[i, col] = new_value

    # Display the updated DataFrame
    st.write("Updated DataFrame:", df)

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
