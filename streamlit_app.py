

import altair as alt
import numpy as np
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
import streamlit as st
import pandas as pd
import io
import zipfile


def home():
    st.title("Home Page")
    st.write("This is the home page.")
    st.markdown("Go to [About](#about)")

def about():
    st.title("About Page")
    st.write("This is the about page.")
    st.markdown("Go to [Home](#home)")

# Define navigation
page = st.sidebar.radio("Navigate", ["Home", "About"])

# Render selected page
if page == "Home":
    home()
elif page == "About":
    about()



def homepage():
    st.title("Home Page")
    st.write("This is the home page.")

def about():
    st.title("About Page")
    st.write("This is the about page.")

def contact():
    st.title("Contact Page")
    st.write("This is the contact page.")

# Sidebar navigation

#Tabs    
tab1, tab2, tab3, tab4,tab5 = st.tabs(["Planned DT", "Routing", "Recovery","Demand","Download"])

data_route = {
    "DPP": ["DPP1", "DPP2", "DPP3","DPP4"],
    "Source": ["OSW-HM", "OSW-HM", "OSW-HM","OSW-HM"],
    "Sink": ["OSW-CM72", "OSW-88", "KIN-CM1","LOG-CM4"],
    "Active":[False,True,False,False]}

data_planned_dt ={"Asset":["OSW-HM","OSW-HM"],
                  "Month":["April 2024","May 2024"],
                  "Hours":[72,24]}

start_date = datetime.now().replace(day=1).date()

# Generate a sequence of dates for the next 18 months
date_range = [start_date + relativedelta(months=i) for i in range(18)]

# Create a DataFrame with the dates
df_demand = pd.DataFrame(date_range, columns=['Date'])
df_demand_pivot = df_demand.transpose()
df_demand_pivot.columns = df_demand_pivot.iloc[0]
df_demand_pivot = df_demand_pivot[1:]


df_route = pd.DataFrame(data_route)
df_data_planned_dt=pd.DataFrame(data_planned_dt)

#Sidebar
st.sidebar.header("Selection Criteria")





with tab1:
   st.header("Planned DT")
   st.data_editor(df_data_planned_dt,num_rows="dynamic")
   st.asset = st.sidebar.multiselect('Select Month',["April","May"])
   
with tab2:
  st.header("Routing")
  st.data_editor(df_route,num_rows="dynamic")
  st.first_filter = st.sidebar.multiselect('Select DPP',["DPP1","DPP2"])
  st.second_filter = st.sidebar.multiselect('Select Source',["OSW-HM"])

with tab3:
  st.header("Recovery")

with tab4:
  st.header("Demand")
  edited_demand_data= st.data_editor(df_demand_pivot,num_rows="dynamic")
  chart_demand_data = edited_demand_data.transpose().apply(pd.to_numeric, errors='coerce')
  st.bar_chart(chart_demand_data)
with tab5:
  st.header("Download")
  csv =  {"route.csv": df_route.to_csv(index=False), 
          "data_planned_dt.csv": df_data_planned_dt.to_csv(index=False),
        "demand_data.csv": df_demand_pivot.to_csv(index=False)}
 


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
  




