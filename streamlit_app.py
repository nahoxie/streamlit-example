import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import pandas as pd

# Create a sample dataframe
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 22],
    "City": ["New York", "Los Angeles", "Chicago"],
}
df = pd.DataFrame(data)

# Display the editable dataframe
edited_df = st.experimental_data_editor(df)
st.write("Edited Dataframe:")
st.write(edited_df)
