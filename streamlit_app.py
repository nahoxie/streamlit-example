
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import pandas as pd


query_name = st.text_input("Filter name")
#query_age = st.text_input2("Filter name")

# Create a sample dataframe
data = {
    "DPP": ["DPP1", "DPP2", "DPP3","DPP4"],
    "Source": ["OSW-HM", "OSW-HM", "OSW-HM","OSW-HM"],
    "Sink": ["OSW-CM72", "OSW-88", "KIN-CM1","LOG-CM4"],
    "Active":[False,True,False,False]
}
df = pd.DataFrame(data)
filtered_df = df[df["DPP"].str.contains(query_name, case=False)]
#filter_df_age = filtered_df[df["Age"].str.contains(query_age, case=False)]
# Display the editable dataframe
edited_df = st.experimental_data_editor(filtered_df)
st.write("Edited Dataframe:")
st.write(edited_df)
