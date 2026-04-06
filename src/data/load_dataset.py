import pandas as pd 
import os 

def load_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found:{file_path}")
    return pd.read.csv(file_path)
#intail loading of the dataset 