
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import pandas as pd




tab1, tab2, tab3 = st.tabs(["Planned DT", "Routing", "Recovery"])

data = {
    "DPP": ["DPP1", "DPP2", "DPP3","DPP4"],
    "Source": ["OSW-HM", "OSW-HM", "OSW-HM","OSW-HM"],
    "Sink": ["OSW-CM72", "OSW-88", "KIN-CM1","LOG-CM4"],
    "Active":[False,True,False,False]}

df = pd.DataFrame(data)
st.sidebar.header("Selection Criteria")
query_name = st.sidebar.text_input("DPP")

first_filter = st.sidebar.multiselect('Select DPP',["DPP1","DPP2"])
df2 = df.query("Source == @first_filter")

# Second filter
second_filter = st.sidebar.multiselect('Select Source',["OSW-HM"])
df3 = df2.query("Source == @second_filter")



with tab1:
   st.header("Planned DT")

   
with tab2:
  st.header("Routing")
edited_df = st.experimental_data_editor(df)
st.write("Edited Dataframe:")
st.write(edited_df)

with tab3:
  st.header("Recovery")
  # Display the editable dataframe


def download_csv(df):
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(label="Download data as CSV", data=csv, file_name='my_dataframe.csv', mime='text/csv')

# Example usage:
st.write(df)  # Display the DataFrame in your Streamlit app
download_csv(df)





