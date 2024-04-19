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
    conn = dbapi.connect(host='adb-3247355026438266.6.azuredatabricks.net', token='dapi422ea597f79c9a7006cfa4c8565efc92')

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




def main():
    st.title("Editable Grid Example")

    # Sample data for the grid
    data = {
        'Name': ['John', 'Alice', 'Bob'],
        'Age': [30, 25, 35],
        'Gender': ['Male', 'Female', 'Male']
    }

    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    # Display the DataFrame as an editable table
    edited_df = st.table(df)

    # Allow users to edit the data
    for i in range(len(df)):
        for col in df.columns:
            # For each cell, create a text input for editing
            new_value = st.text_input(f'Edit {col} for row {i+1}', df.iloc[i][col])
            # Update the DataFrame with the new value
            df.at[i, col] = new_value

    # Display the updated DataFrame
    st.write("Updated DataFrame:", df)

if __name__ == "__main__":
    main()

