import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

import sqlalchemy

"""
# Welcome to the New S&OP Routing Generator!


"""



def main():
    st.title("Data Retrieval from Databricks Example")


host = "adb-3247355026438266.6.azuredatabricks.net"
http_path = "sql/protocolv1/o/3247355026438266/0624-130121-wads668"
token = db_key

# Create the SQLAlchemy engine
engine = sqlalchemy.create_engine(
    f"databricks+odbc://token:{token}@{host}{http_path}"
)

query = "Select machine_downtime_key,downtime_duration_hrs,site_key from dap_enterprise.machine_downtime limit 10"
data = pd.read_sql(query)

# Display the retrieved data in Streamlit
st.write("Data from Databricks:", data)

if __name__ == "__main__":
    main()
