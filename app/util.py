import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import seaborn as sns


def upload_data(uploaded_file):
    if uploaded_file is not None:
        return uploaded_file
    else:
        return None


def time_series_analysis(columns, data=None):
    # Convert 'Timestamp' column to datetime format (assuming it exists)
    if 'Timestamp' in data.columns:
        data['Timestamp'] = pd.to_datetime(data['Timestamp'])

    # Create the time series plot
    fig, ax = plt.subplots(figsize=(12, 6))
    for col in columns:
        ax.plot(data['Timestamp'], data[col], label=col)
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Value')
    ax.set_title('Time Series Plot')
    ax.legend()

    # Display the plot using Streamlit's st.pyplot()
    st.pyplot(fig)


def correlation_analysis(group_name1, group_cols1, group_name2, group_cols2, data):

    all_cols = group_cols1 + group_cols2
    correlation_matrix = data[all_cols].corr()
    group1_matrix = correlation_matrix.loc[group_cols1, group_cols2]

    # Create the correlation heatmap
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(group1_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    ax.set_title(f'Correlation Heatmap ({group_name1} vs. {group_name2})')

    # Display the plot using Streamlit's st.pyplot()
    st.pyplot(fig)


def wind_analysis(wind_speed_cols, wind_direction_cols, data):
    if 'Timestamp' in data.columns:
        data['Timestamp'] = pd.to_datetime(data['Timestamp'])

    wind_speed_to_plot = [col for col in wind_speed_cols if col in data.columns]
    wind_direction_to_plot = [col for col in wind_direction_cols if col in data.columns]

    if wind_speed_to_plot:
        fig, ax = plt.subplots(figsize=(12, 6))
        for col in wind_speed_to_plot:
            ax.plot(data['Timestamp'], data[col], label=col)
        ax.set_xlabel('Timestamp')
        ax.set_ylabel('Speed (m/s)')
        ax.set_title('Wind Speed Analysis')
        ax.legend()
        st.pyplot(fig)

    if wind_direction_to_plot:
        fig, ax = plt.subplots(figsize=(12, 6))
        for col in wind_direction_to_plot:
            ax.plot(data['Timestamp'], data[col], label=col)
        ax.set_xlabel('Timestamp')
        ax.set_ylabel('Direction (°)')
        ax.set_title('Wind Direction Analysis')
        ax.legend()
        st.pyplot(fig)


def temperature_analysis(temperature_cols, data, module_temp_prefix='TMod', ambient_temp_name='Tamb'):
    if 'Timestamp' in data.columns:
        data['Timestamp'] = pd.to_datetime(data['Timestamp'])

    available_temp_cols = [col for col in temperature_cols if col in data.columns]

    if available_temp_cols:
        fig, ax = plt.subplots(figsize=(12, 6))
        for col in available_temp_cols:
            ax.plot(data['Timestamp'], data[col], label=col)
        ax.set_xlabel('Timestamp')
        ax.set_ylabel('Temperature (°C)')
        ax.set_title('Temperature Analysis')
        ax.legend()
        st.pyplot(fig)

    module_temp_cols = [col for col in available_temp_cols if col.startswith(module_temp_prefix)]
    ambient_temp_col = [col for col in available_temp_cols if col == ambient_temp_name]

    if module_temp_cols and ambient_temp_col:
        for col in module_temp_cols:
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.scatter(data[col], data[ambient_temp_col[0]], alpha=0.5)  
            ax.set_xlabel(f'{col} (°C)')
            ax.set_ylabel('Ambient Temperature (°C)')
            ax.set_title(f'{col} vs Ambient Temperature')
            ax.grid(True)
            st.pyplot(fig)


def histograms(columns, data):
    available_cols = [col for col in columns if col in data.columns]
    if not available_cols:
        raise ValueError("No columns found in the data for creating histograms.")

    for i, col in enumerate(available_cols):
        plt.figure(figsize=(8, 6))
        plt.hist(data[col], bins=20, edgecolor='black')
        plt.title(f'Histogram of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        st.pyplot()



def box_plots(columns, data):
    available_cols = [col for col in columns if col in data.columns]
    if not available_cols:
        raise ValueError("No columns found in the data for creating box plots.")

    for i, col in enumerate(available_cols):
        plt.figure(figsize=(8, 6))
        sns.boxplot(y=data[col]) 
        plt.title(f'Box Plot of {col}')
        st.pyplot()


def scatter_plot(x_col, y_col, data):
    if x_col not in data.columns or y_col not in data.columns:
        raise ValueError(f"Columns '{x_col}' and '{y_col}' not found in the data.")

    plt.figure(figsize=(8, 6))
    plt.scatter(data[x_col], data[y_col], alpha=0.5)
    plt.title(f'{x_col} vs. {y_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True)
    st.pyplot()