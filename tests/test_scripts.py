import os
import sys
import unittest
import pandas as pd

# Add the project root to sys.path
cwd = os.getcwd()
project_root = os.path.dirname(cwd)
sys.path.append(project_root)

from scripts.data_analysis_utils import DataAnalysis

class TestDataAnalysis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.file_path = "../data/benin-malanville.csv" 
        cls.data_analyzer = DataAnalysis(cls.file_path)
        cls.data_analyzer.load_data()

    def test_load_data(self):
        self.assertIsNotNone(self.data_analyzer.df)
        self.assertIsInstance(self.data_analyzer.df, pd.DataFrame)

    def test_summary_statistics(self):
        summary_stats = self.data_analyzer.summary_statistics()
        self.assertIsNotNone(summary_stats)
        self.assertIsInstance(summary_stats, pd.DataFrame)

    def test_data_quality_check(self):
        columns = ['GHI', 'DNI', 'DHI']
        results = self.data_analyzer.data_quality_check(columns)
        self.assertIsNotNone(results)
        self.assertIsInstance(results, dict)

    def test_time_series_analysis(self):
        columns = ['GHI', 'DNI', 'DHI', 'Tamb']
        with self.assertRaises(ValueError):
            self.data_analyzer.time_series_analysis(columns)

    def test_correlation_analysis(self):
   
        group_name1 = "Solar Radiation" 
        group_cols1 = ['GHI', 'DNI', 'DHI'] 
        group_name2 = "Temperature"
        group_cols2 = ['TModA', 'TModB']
        with self.assertRaises(ValueError):
            self.data_analyzer.correlation_analysis(group_name1, group_cols1, group_name2, group_cols2)

    def test_wind_analysis(self):
        wind_speed_cols = ['WS', 'WSgust', 'WSstdev'] 
        wind_direction_cols = ['WD', 'WDstdev']  
        with self.assertRaises(ValueError):
            self.data_analyzer.wind_analysis(wind_speed_cols, wind_direction_cols)

    def test_temperature_analysis(self):
        temperature_cols = ['TModA', 'TModB', 'Tamb'] 
        with self.assertRaises(ValueError):
            self.data_analyzer.temperature_analysis(temperature_cols)

    def test_histograms(self):
        columns = ['GHI', 'DNI', 'DHI', 'WS', 'TModA', 'TModB', 'Tamb']
        with self.assertRaises(ValueError):
            self.data_analyzer.histograms(columns)

    def test_box_plots(self):
        columns = ['GHI', 'DNI', 'DHI']
        with self.assertRaises(ValueError):
            self.data_analyzer.box_plots(columns)

    def test_scatter_plot(self):
        x_col = "GHI"
        y_col = "Tamb"
        with self.assertRaises(ValueError):
            self.data_analyzer.scatter_plot(x_col, y_col)

    def test_data_cleaning(self):
        with self.assertRaises(ValueError):
            self.data_analyzer.data_cleaning()

if __name__ == '__main__':
    unittest.main()