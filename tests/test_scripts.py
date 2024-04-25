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

if __name__ == '__main__':
    unittest.main()