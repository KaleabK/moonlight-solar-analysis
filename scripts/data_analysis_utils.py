import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataAnalysis:
    """
    A reusable class for data analysis tasks.

    Attributes:
        file_path (str): Path to the data file.
        df (pd.DataFrame, None): Loaded DataFrame, initialized to None.
    """

    def __init__(self, file_path):
        """
        Initializes the DataAnalysis object with the file path.

        Args:
            file_path (str): Path to the data file.
        """
        self.file_path = file_path
        self.df = None


    def load_data(self):
        """
        Loads the data from the provided file path into a pandas DataFrame.

        Returns:
            pd.DataFrame: The loaded DataFrame on success, None otherwise.
        """
        try:
            self.df = pd.read_csv(self.file_path)
            print("Dataset loaded successfully!")
            return self.df  # Return the DataFrame for chaining
        except FileNotFoundError:
            print("File not found. Please provide a valid file path.")
            return None  # Return None on error


    def summary_statistics(self, data=None):
        """
        Calculates and returns summary statistics of the loaded data.

        Raises:
            ValueError: If the data is not loaded.

        Returns:
            pd.DataFrame: The summary statistics DataFrame, None if data not loaded.
        """
        if data is None:
            self.check_data_loaded()
            data = self.df  # Use self.df if no data argument provided
        summary_stats = data.describe()
        return summary_stats


    def check_data_loaded(self):
        """
        Helper function to check if data is loaded before performing operations.

        Raises:
            ValueError: If the data is not loaded.
        """
        if self.df is None:
            raise ValueError("Dataset not loaded. Please load the data first.")


    def data_quality_check(self, columns, data=None):
        """
        Performs basic data quality checks on the specified columns of the loaded data (self.df)
        or provided data (if specified).

        Checks for missing values, negative values, and outliers (using z-scores).

        Args:
            data (pandas.DataFrame, optional): The DataFrame to perform checks on.
                Defaults to None, in which case self.df is used.
            columns (list): A list of column names to perform checks on.

        Raises:
            ValueError: If the data is not loaded and no data argument is provided.

        Returns:
            dict: A dictionary containing the results of the checks for each column
                (missing_values, negative_values, outliers).
        """
        if data is None:
            self.check_data_loaded()
            data = self.df  # Use self.df if no data argument provided

        missing_values = data[columns].isnull().sum()
        negative_values = (data[columns] < 0).sum()

        # Calculate z-scores for specified columns
        z_scores = data[columns].apply(lambda x: (x - x.mean()) / x.std())
        outliers = (z_scores > 3).sum()

        results = {col: {
            "missing_values": missing_values[col],
            "negative_values": negative_values[col],
            "outliers": outliers[col]
        } for col in columns}

        return results
    

    def time_series_analysis(self, columns, data=None) :
        """
        Performs time series analysis on the specified columns of the loaded data (self.df)
        or provided data (if specified).

        Converts the 'Timestamp' column to datetime format (assuming it exists) and plots
        the values of the specified columns over time.

        Args:
            data (pandas.DataFrame, optional): The DataFrame to perform time series analysis on.
                Defaults to None, in which case self.df is used.
            columns (list): A list of column names to plot in the time series.

        Raises:
            ValueError: If the data is not loaded and no data argument is provided.
        """
        if data is None:
            self.check_data_loaded()
            data = self.df  # Use self.df if no data argument provided

        # Convert 'Timestamp' column to datetime format (assuming it exists)
        if 'Timestamp' in data.columns:
            data['Timestamp'] = pd.to_datetime(data['Timestamp'])

        # Create the time series plot
        plt.figure(figsize=(12, 6))
        for col in columns:
            plt.plot(data['Timestamp'], data[col], label=col)
        plt.xlabel('Timestamp')
        plt.ylabel('Value')
        plt.title('Time Series Plot')
        plt.legend()
        plt.show()


    def correlation_analysis(self, group_name1, group_cols1, group_name2, group_cols2, data=None):
        """
        Performs correlation analysis on the specified columns of the loaded data (self.df)
        or provided data (if specified).

        Calculates the correlation matrix for variables in group1 with variables in group2
        and plots a heatmap to visualize correlations.

        Args:
           
            group_name1 (str): Name for the first group of columns.
            group_cols1 (list): A list of column names from the first group.
            group_name2 (str): Name for the second group of columns.
            group_cols2 (list): A list of column names from the second group.
            data (pandas.DataFrame, optional): The DataFrame to perform correlation analysis on.
                Defaults to None, in which case self.df is used.

        Raises:
            ValueError: If the data is not loaded and no data argument is provided.
        """
        if data is None:
            self.check_data_loaded()
            data = self.df  # Use self.df if no data argument provided

        # Combine columns from both groups for correlation calculation
        all_cols = group_cols1 + group_cols2

        # Calculate correlation matrix using all columns
        correlation_matrix = data[all_cols].corr()

        # Select the sub-matrix containing correlations between the two groups
        group1_matrix = correlation_matrix.loc[group_cols1, group_cols2]

        # Create the correlation heatmap (adjust figure size and other options as needed)
        plt.figure(figsize=(10, 8))
        sns.heatmap(group1_matrix, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title(f'Correlation Heatmap ({group_name1} vs. {group_name2})')
        plt.show()


    def wind_analysis(self,wind_speed_cols, wind_direction_cols, data=None):
        """
        Performs wind analysis on the specified columns of the loaded data (self.df)
        or provided data (if specified).

        Plots wind speed (including standard deviation) and wind direction (including standard deviation)
        over time, considering only columns that exist in the data.

        Args:
            data (pandas.DataFrame, optional): The DataFrame to perform wind analysis on.
                Defaults to None, in which case self.df is used.
            wind_speed_cols (list): A list of column names for wind speed analysis (e.g., 'WS', 'WSgust', 'WSstdev').
            wind_direction_cols (list): A list of column names for wind direction analysis (e.g., 'WD', 'WDstdev').

        Raises:
            ValueError: If no wind-related columns are provided for analysis (even after checking data).
        """
        if data is None:
            self.check_data_loaded()
            data = self.df  # Use self.df if no data argument provided

        # Convert 'Timestamp' column to datetime format (assuming it exists)
        if 'Timestamp' in data.columns:
            data['Timestamp'] = pd.to_datetime(data['Timestamp'])

        # Check if any wind-related columns exist in the data after potentially cleaning
        wind_speed_to_plot = [col for col in wind_speed_cols if col in data.columns]
        wind_direction_to_plot = [col for col in wind_direction_cols if col in data.columns]

        # Handle case where no wind-related columns are available for plotting
        if not wind_speed_to_plot and not wind_direction_to_plot:
            raise ValueError("No wind-related columns found in the data for analysis.")

        # Plot wind speed over time
        if wind_speed_to_plot:
            plt.figure(figsize=(12, 6))
            for col in wind_speed_to_plot:
                plt.plot(data['Timestamp'], data[col], label=col)
            plt.xlabel('Timestamp')
            plt.ylabel('Speed (m/s)')
            plt.title('Wind Speed Analysis')
            plt.legend()
            plt.show()

        # Plot wind direction over time
        if wind_direction_to_plot:
            plt.figure(figsize=(12, 6))
            for col in wind_direction_to_plot:
                plt.plot(data['Timestamp'], data[col], label=col)
            plt.xlabel('Timestamp')
            plt.ylabel('Direction (°)')
            plt.title('Wind Direction Analysis')
            plt.legend()
            plt.show()


    def temperature_analysis(self, temperature_cols, module_temp_prefix='TMod', ambient_temp_name='Tamb', data=None):
        """
        Performs temperature analysis on the specified columns of the loaded data (self.df)
        or provided data (if specified).

        Plots temperature over time and scatter plots between module and ambient temperatures,
        considering only columns that exist in the data.

        Args:
            data (pandas.DataFrame, optional): The DataFrame to perform temperature analysis on.
                Defaults to None, in which case self.df is used.
            temperature_cols (list): A list of column names for temperature analysis.
            module_temp_prefix (str, optional): Prefix for identifying module temperature columns (default: 'TMod').
            ambient_temp_name (str, optional): Name of the ambient temperature column (default: 'Tamb').

        Raises:
            ValueError: If no temperature columns are found in the data for analysis (even after checking).
        """
        if data is None:
            self.check_data_loaded()
            data = self.df  # Use self.df if no data argument provided

        # Convert 'Timestamp' column to datetime format (assuming it exists)
        if 'Timestamp' in data.columns:
            data['Timestamp'] = pd.to_datetime(data['Timestamp'])

        # Check if any temperature columns exist in the data after potentially cleaning
        available_temp_cols = [col for col in temperature_cols if col in data.columns]

        # Handle case where no temperature columns are available for plotting
        if not available_temp_cols:
            raise ValueError("No temperature columns found in the data for analysis.")

        # Plot temperature over time
        if available_temp_cols:
            plt.figure(figsize=(12, 6))
            for col in available_temp_cols:
                plt.plot(data['Timestamp'], data[col], label=col)
            plt.xlabel('Timestamp')
            plt.ylabel('Temperature (°C)')
            plt.title('Temperature Analysis')
            plt.legend()
            plt.show()

        # Identify module and ambient temperature columns based on prefixes and names
        module_temp_cols = [col for col in available_temp_cols if col.startswith(module_temp_prefix)]
        ambient_temp_col = [col for col in available_temp_cols if col == ambient_temp_name]

        # Scatter plots between module and ambient temperatures (if columns exist)
        if module_temp_cols and ambient_temp_col:
            for col in module_temp_cols:
                plt.figure(figsize=(8, 6))
                plt.scatter(data[col], data[ambient_temp_col[0]], alpha=0.5)  # Assuming one ambient temp column
                plt.xlabel(f'{col} (°C)')
                plt.ylabel('Ambient Temperature (°C)')
                plt.title(f'{col} vs Ambient Temperature')
                plt.grid(True)
                plt.show()


    def histograms(self, columns, data=None):
        """
        Creates histograms for specified columns in the loaded data (self.df)
        or provided data (if specified).

        Args:
            data (pandas.DataFrame, optional): The DataFrame to create histograms for.
                Defaults to None, in which case self.df is used.
            columns (list): A list of column names to create histograms for.

        Raises:
            ValueError: If no columns are provided for creating histograms (even after checking data).
        """
        if data is None:
            self.check_data_loaded()
            data = self.df  # Use self.df if no data argument provided

        available_cols = [col for col in columns if col in data.columns]
        if not available_cols:
            raise ValueError("No columns found in the data for creating histograms.")

        n_rows = int((len(available_cols) - 1) / 3) + 1  # Calculate number of rows for subplots
        n_cols = min(3, len(available_cols))  # Determine number of columns for subplots

        plt.figure(figsize=(12, n_rows * 3))

        for i, col in enumerate(available_cols):
            plt.subplot(n_rows, n_cols, i + 1)
            plt.hist(data[col], bins=20, edgecolor='black')
            plt.title(f'Histogram of {col}')
            plt.xlabel(col)
            plt.ylabel('Frequency')

        plt.tight_layout()
        plt.show()


    def box_plots(self, columns, data=None):
        """
        Creates box plots for specified columns in the loaded data (self.df)
        or provided data (if specified).

        Args:
            data (pandas.DataFrame, optional): The DataFrame to create box plots for.
                Defaults to None, in which case self.df is used.
            columns (list): A list of column names to create box plots for.

        Raises:
            ValueError: If no columns are found in the data for creating box plots (even after checking data).
        """
        if data is None:
            self.check_data_loaded()
            data = self.df  # Use self.df if no data argument provided

        available_cols = [col for col in columns if col in data.columns]
        if not available_cols:
            raise ValueError("No columns found in the data for creating box plots.")

        n_rows = int((len(available_cols) - 1) / 3) + 1  # Calculate number of rows for subplots
        n_cols = min(3, len(available_cols))  # Determine number of columns for subplots

        plt.figure(figsize=(12, n_rows * 3))

        for i, col in enumerate(available_cols):
            plt.subplot(n_rows, n_cols, i + 1)
            sns.boxplot(y=data[col]) 
            plt.title(f'Box Plot of {col}')

        plt.tight_layout()
        plt.show()


    def scatter_plot(self, x_col, y_col, data=None):
        """
        Creates a scatter plot to visualize the relationship between two variables in the 
        loaded data (self.df) or provided data (if specified).

        Args:
            data (pandas.DataFrame, optional): The DataFrame to create a scatter plot for.
                Defaults to None, in which case self.df is used.
            x_col (str): Name of the column for the x-axis.
            y_col (str): Name of the column for the y-axis.

        Raises:
            ValueError: If the specified columns are not found in the data (even after checking).
        """
        if data is None:
            self.check_data_loaded()
            data = self.df  # Use self.df if no data argument provided

        # Check if x_col and y_col exist in the data
        if x_col not in data.columns or y_col not in data.columns:
            raise ValueError(f"Columns '{x_col}' and '{y_col}' not found in the data.")

        plt.figure(figsize=(8, 6))
        plt.scatter(data[x_col], data[y_col], alpha=0.5)
        plt.title(f'{x_col} vs. {y_col}')
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.grid(True)
        plt.show()


    def data_cleaning(self, drop_comments=True, handle_missing_values='dropna', columns_to_clean=None):
        """
        Performs data cleaning operations on the loaded data.

        Args:
            drop_comments (bool, optional): Whether to drop the 'Comments' column if entirely null (default: True).
            handle_missing_values (str, optional): Method to handle missing values ('dropna').
            columns_to_clean (list, optional): List of column names for outlier handling (default: None).

        Returns:
            pandas.DataFrame: The cleaned DataFrame.

        Raises:
            ValueError: If the data is not loaded.
        """
        self.check_data_loaded()

        df_cleaned = self.df.copy()  # Avoid modifying the original data

        # Drop 'Comments' column if entirely null
        if drop_comments and pd.isnull(df_cleaned['Comments']).all():
            df_cleaned.drop(columns='Comments', inplace=True)

        # Handle missing values
        if handle_missing_values == 'dropna':
            df_cleaned.dropna(inplace=True)
        elif callable(handle_missing_values):
            df_cleaned = handle_missing_values(df_cleaned.copy())  # Avoid modifying cleaned data within function
        else:
            print(f"Warning: Invalid method '{handle_missing_values}' for handling missing values.")

        # Handle negative values
        if columns_to_clean is None:
            columns_to_clean = []
        special_columns = ['GHI', 'DNI', 'DHI']
        for col in df_cleaned.columns:
            if col in columns_to_clean or col in special_columns:
                if col in special_columns: 
                    # Change sign of negative values
                    df_cleaned.loc[df_cleaned[col] < 0, col] *= -1
                else:
                    pass

        df_cleaned = df_cleaned.reset_index(drop=True)

        return df_cleaned