import os
import sys
import streamlit as st

cwd = os.getcwd()
project_root = os.path.dirname(cwd)
sys.path.append(project_root + '/moonlight-solar-analysis')
from util import *


from scripts.data_analysis_utils import DataAnalysis
# Function to handle data upload


st.title("Solar Irradiance Analysis Dashboard")
st.write("This dashboard explores solar irradiance data to understand energy generation potential.")


# Data Upload
uploaded_data = upload_data(st.file_uploader("Upload Your Solar Irradiance Data (CSV)", type="csv"))

if uploaded_data is not None:
    # Initialize DataAnalysis object
    data_analysis = DataAnalysis(uploaded_data)

    # Load data
    data = data_analysis.load_data()

    # Dropdown for selecting analysis type
    selected_analysis = st.selectbox("Select Analysis Type", [
        "Summary Statistics", 
        "Data Quality Check", 
        "Time Series Analysis",
        "Correlation Analysis",
        "Wind Analysis",
        "Temperature Analysis",
        "Histograms",
        "Box Plots",
        "Scatter Plot"
    ])
    
    if selected_analysis == "Summary Statistics":
        st.subheader("Summary Statistics")
        st.write(data_analysis.summary_statistics())

    elif selected_analysis == "Data Quality Check":
        st.subheader("Data Quality Check")
        columns_for_quality_check = st.multiselect("Select columns for Time Series Analysis", data_analysis.df.columns)
        st.write(data_analysis.data_quality_check(columns_for_quality_check))

    elif selected_analysis == "Time Series Analysis":
        st.subheader("Time Series Analysis")
        columns_for_time_series = st.multiselect("Select columns for Time Series Analysis", data_analysis.df.columns)
        if columns_for_time_series:
            time_series_analysis(columns_for_time_series, data)

    elif selected_analysis == "Correlation Analysis":
        st.subheader("Correlation Analysis")
        st.write("Select two groups of columns for correlation analysis:")
        group1_name = st.text_input("Group 1 Name", value="Solar Radiation")
        group1_columns = st.multiselect("Group 1 Columns", data_analysis.df.columns)
        group2_name = st.text_input("Group 2 Name", value="Temperature")
        group2_columns = st.multiselect("Group 2 Columns", data_analysis.df.columns)
        if group1_columns and group2_columns:
            correlation_analysis(group1_name, group1_columns, group2_name, group2_columns,data)

    elif selected_analysis == "Wind Analysis":
        st.subheader("Wind Analysis")
        wind_speed_cols = st.multiselect("Wind Speed Columns", data_analysis.df.columns)
        wind_direction_cols = st.multiselect("Wind Direction Columns", data_analysis.df.columns)
        if wind_direction_cols and wind_direction_cols:
            wind_analysis(wind_speed_cols, wind_direction_cols,data)

    elif selected_analysis == "Temperature Analysis":
        st.subheader("Temperature Analysis")
        temperature_cols = st.multiselect("Temprature Columns", data_analysis.df.columns)
        if temperature_cols:
            temperature_analysis(temperature_cols,data)

    elif selected_analysis == "Histograms":
        st.subheader("Histograms")
        columns_for_histograms = st.multiselect("Select columns for Histograms", data_analysis.df.columns)
        if columns_for_histograms:
            histograms(columns_for_histograms,data)

    elif selected_analysis == "Box Plots":
        st.subheader("Box Plots")
        columns_for_box_plots = st.multiselect("Select columns for Box Plots", data_analysis.df.columns)
        if columns_for_box_plots:
            box_plots(columns_for_box_plots,data)

    elif selected_analysis == "Scatter Plot":
        st.subheader("Scatter Plot")
        x_col = st.selectbox("Select X-axis column", data_analysis.df.columns)
        y_col = st.selectbox("Select Y-axis column", data_analysis.df.columns)
        if x_col and y_col:
            scatter_plot(x_col, y_col,data)

else:
    st.write("No data uploaded yet. Please upload a CSV file.")
