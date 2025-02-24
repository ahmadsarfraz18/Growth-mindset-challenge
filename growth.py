
import streamlit as st 
import pandas as pd 
import os
from io import BytesIO

st.set_page_config(page_title = "data sweeper", layout= "wide")


# Custom Css...

st.markdown(
    """
    <style>
    .stApp{
        background-color: black;
        color: white
        }
        </style>

        """,

        unsafe_allow_html= True

)

# Title and Description... 

st.title ("✨Datasweeper Sterling Intergrator By Mahar Ahmad Sarfraz✨")
st.write ("Transform your files between CSV and Excel formats with built-in data cleaning and visualization creating the project fro quarter 3 !")

# File Uploader... 

Uploaded_files = st.file_uploader ("Upload your files (Accepts only CSV or Excel):", type= ["csv", "xlsx"], accept_multiple_files=(True))

if Uploaded_files:
    for file in Uploaded_files:
        file_ext = os.path.splitext(file.name) [-1].lower ()

        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == "xlsx":
            df = pd.read_excel(file)
        else:
             st.error (f"Unsupported file type: {file_ext}")
             continue

    # File Details... 

    st.write ("📀 Preview the head of the Dataframe")
    st.dataframe (df.head())

    # Data Cleaning Options ...

    st.subheader("💥 Data Cleaning Options")

    if st.checkbox (f"Cleaning data for {file.name}"):
        col1 , col2 = st.columns (2)

        with col1:
            if st.button (f"Reomove the duplicates from the file {file.name}"):
                df.drop_duplicates(inplace = True)
                st.write ("✅ Duplicates Removed !")

        with col2: 
            if st.button (f"Fill missing vaules for {file.name}"):
                numeric_col = df.select_dtypes(include= ['number']).columns
                df[numberic_col] = df[numeric_col].fillna (df[numeric_cols].mean())
                st.write ("✅ Missing values have been filled !")
    st.subheader ("💟 Select columns to keep")
    columns = st.multiselect(f"Choose columns for {file.name}", df.columns, default = df.columns)
    df = df[columns]

    # Data Visualization...

    st.subheader ("👔 Data Visualization")
    if st.checkbox(f"Show visualization for {file.name}"):
        st.bar_chart(df.select_dtypes(inculde = 'number').iloc[:, :2])

# Conversion Options... 

st.subheader ("🎉 Conversion Options")
conversion_type = st.radio (f"Convert {file.name} to:", ['csv', 'xlsx'], key = file.name)
if st.button (f"Conver {file.name}"):
    buffer = BytesIO()
    if conversion_type == "CSV":
        df.to.csv (buffer, index = False)
        file_name = file.name.replace(file_ext, ".csv")
        mime_type = "text/csv"

    elif conversion_type == "Excel":
        df.to_excel (buffer, index = False)
        file_name = file.name.replace (file_ext, ".xlsx")
        mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        buffer.seek(0)

        st.download_button(
            label= f"Download {file.name} as {conversion_type}",
            data= buffer,
            file_name = file_name,
            mime = mime_type
        )
st.success ("🎉 All files processed successfully!")
