
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import pandas as pd


query_name = st.text_input("Filter name")
query_age = st.text_input("Filter name")

# Create a sample dataframe
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 22],
    "City": ["New York", "Los Angeles", "Chicago"],
}
df = pd.DataFrame(data)
filtered_df = df[df["Name"].str.contains(query_name, case=False)]
#filter_df_age = filtered_df[df["Age"].str.contains(query_age, case=False)]
# Display the editable dataframe
edited_df = st.experimental_data_editor(filtered_df)
st.write("Edited Dataframe:")
st.write(edited_df)
