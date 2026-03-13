import pandas as pd

def load_data(file_path):

    #loads insurance data from a pipe-delimited csv file.

    try:

        df = pd.read_csv(file_path, sep = '|')
        print(f" Successfuly loaded data from {file_path}")

        return df
    except Exception as e:
        print(f"Error loading data: {e}")

        return None