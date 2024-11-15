import unittest
from unittest.mock import patch
import pandas as pd
from io import StringIO


import sys
import os

# # Add the parent directory to the system path
sys.path.append(os.path.abspath('../scripts'))
sys.path.append(os.path.abspath('../tests'))

from data_processing import load_data

class TestLoadData(unittest.TestCase):

    @patch('logging.info')  # Mocking the logging.info method
    def test_load_data(self, mock_logging_info):
        # Sample CSV data
        csv_data = """Date,Price
2024-01-01,100
2024-01-02,150
2024-01-03,NaN
2024-01-04,200"""
        
        # Using StringIO to mock file reading (as if it's a real file)
        test_data = StringIO(csv_data)
        
        # Call the load_data function
        df = load_data(test_data)
        
        # Check if the data was loaded correctly
        self.assertEqual(len(df), 4)  # Check if 4 rows are loaded
        self.assertEqual(df.index.name, 'Date')  # Check if 'Date' is set as the index
        self.assertTrue(pd.to_datetime(df.index).equals(pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04'])))  # Check if dates are correct
        self.assertTrue(df['Price'].isna().sum() == 0)  # Check if NaN in 'Price' column is interpolated
        
        # Check if logging was called
        mock_logging_info.assert_any_call("Loading data from file...")
        mock_logging_info.assert_any_call("Data loaded ")

if __name__ == '__main__':
    unittest.main()
