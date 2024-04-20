
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import pandas as pd
import io
import zipfile



tab1, tab2, tab3, tab4 = st.tabs(["Planned DT", "Routing", "Recovery","Download"])

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

csv =  {"data1.csv": df_route.to_csv(index=False), 
          "data2.csv": df_data_planned_dt.to_csv(index=False)}
 


zip_buffer = io.BytesIO()
with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
    for file_name, data in csv.items():
        zip_file.writestr(file_name, data.encode("utf-8"))

# Display a download button for the zip file
st.download_button(
    label="Download All DataFrames as Zip",
    data=zip_buffer,
    file_name="my_dataframes.zip",
    mime="application/zip",
)

with tab1:
   st.header("Planned DT")
   st.data_editor(df_data_planned_dt)
  
   
with tab2:
  st.header("Routing")
  st.data_editor(df_route)
  
with tab3:
  st.header("Recovery")

with tab4:
  st.header("Download")
  
 
  




