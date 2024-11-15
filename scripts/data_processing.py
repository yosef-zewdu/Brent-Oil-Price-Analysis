import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import logging



# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Load Data 
def load_data(path):
    ''' 
    Function to Load Data from csv files

    '''
    logging.info("Loading data from file...")
    
    # Read the files with low_memory=False 
    df = pd.read_csv(path)

    df['Date'] = pd.to_datetime(df['Date'], format='mixed', errors='coerce')
    df = df.sort_values(by='Date')
    df = df.set_index('Date')

    # Preprocess the df
    df['Price'] = df['Price'].interpolate()
    
    # Set pandas display options
    pd.set_option('display.max_columns', None)
    
    logging.info(f"Data loaded ")
    return df

