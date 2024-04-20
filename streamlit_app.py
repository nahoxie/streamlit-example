
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import pandas as pd




tab1, tab2, tab3 = st.tabs(["Planned DT", "Routing", "Recovery"])

data_route = {
    "DPP": ["DPP1", "DPP2", "DPP3","DPP4"],
    "Source": ["OSW-HM", "OSW-HM", "OSW-HM","OSW-HM"],
    "Sink": ["OSW-CM72", "OSW-88", "KIN-CM1","LOG-CM4"],
    "Active":[False,True,False,False]}

data_planned_dt ={"Asset":["OSW-HM","OSW-HM"],
                  "Month":["April 2024","May 2024"],
                  "Hours":[72,24]}

df_route = pd.DataFrame(data_route)
df_data_planned_dt=pd.DataFrame(data_planned_dt)

#Sidebar
st.sidebar.header("Selection Criteria")
first_filter = st.sidebar.multiselect('Select DPP',["DPP1","DPP2"])
second_filter = st.sidebar.multiselect('Select Source',["OSW-HM"])




with tab1:
   st.header("Planned DT")
   st.edited_df_planned_dt = st.experimental_data_editor(df_data_planned_dt)
   st.write(edited_df_planned_dt)
   
with tab2:
  st.header("Routing")
  st.edited_df = st.experimental_data_editor(df)
  st.write("Edited Dataframe:")
  st.write(edited_df)

with tab3:
  st.header("Recovery")


def download_csv(df):
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(label="Download data as CSV", data=csv, file_name='my_dataframe.csv', mime='text/csv')

# Example usage:
download_csv(df)





