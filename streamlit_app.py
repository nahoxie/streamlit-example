import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to the New S&OP Routing Generator!


"""

from databricks import dbapi

def main():
    st.title("Data Retrieval from Databricks Example")

    # Connect to Databricks cluster
    conn = dbapi.connect(host='adb-3247355026438266.6.azuredatabricks.net', token=DB_KEY)

    # Execute SQL query to retrieve data
    cursor = conn.cursor()
    cursor.execute('Select machine_downtime_key,downtime_duration_hrs,site_key from dap_enterprise.machine_downtime limit 10')
    data = cursor.fetchall()

    # Display the retrieved data in Streamlit
    st.write("Data from Databricks:", data)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
