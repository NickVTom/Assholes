def load_data_from_excel(file_path):
    """
    Load data from an Excel file into a pandas DataFrame.
    
    Parameters:
    - file_path: str, path to the Excel file.
    
    Returns:
    - DataFrame containing the loaded data.
    """
    import pandas as pd
    return pd.read_excel(file_path)

