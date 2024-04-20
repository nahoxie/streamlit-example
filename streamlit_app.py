
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import pandas as pd

data = {
    "DPP": ["DPP1", "DPP2", "DPP3","DPP4"],
    "Source": ["OSW-HM", "OSW-HM", "OSW-HM","OSW-HM"],
    "Sink": ["OSW-CM72", "OSW-88", "KIN-CM1","LOG-CM4"],
    "Active":[False,True,False,False]
}
df = pd.DataFrame(data)


st.sidebar.header("This is a Test")

query_name = st.sidebar.text_input("DPP")

first_filter = st.multiselect("Select DPP", default=["DPP1","DPP2"])
df2 = df.query("Source == @first_filter")

# Second filter
second_filter = st.sidebar.multiselect("Select Source",default=["OSW-HM"])
df3 = df2.query("Source == @second_filter")


# Create a sample dataframe


# Display the editable dataframe
edited_df = st.experimental_data_editor(df3)
st.write("Edited Dataframe:")
st.write(edited_df)
