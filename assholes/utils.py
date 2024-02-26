def read_excel(file_path):
    """
    Load data from an Excel file into a pandas DataFrame.
    
    Parameters:
    - file_path: str, path to the Excel file.
    
    Returns:
    - DataFrame containing the loaded data.
    """
    import pandas as pd
    return pd.read_excel(file_path)

def create_pie(file_path, categories_column, values_column, title=''):
    """
    Create and display a pie chart from Excel data.
    
    Parameters:
    - file_path: str, path to the Excel file.
    - categories_column: str, name of the column containing category labels.
    - values_column: str, name of the column containing the values for each category.
    - title: str, title of the pie chart.
    """
    import pandas as pd
    import matplotlib.pyplot as plt

    # Use the existing function to read data from Excel
    data = read_excel(file_path)

    # Extract categories and values based on provided column names
    categories = data[categories_column]
    values = data[values_column]

    # Create the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=categories, autopct='%1.1f%%')
    plt.title(title)
    plt.show()
    
def create_bar(file_path):
    # Load the data from an Excel file
    wb = pd.read_excel(file_path)
    
    # Count the occurrences of each 'Status'
    status_counts = wb.groupby('Status')['Status'].count()
    
    # Get the unique statuses and their counts
    statuses = status_counts.index.tolist()
    counts = status_counts.values.tolist()
    
    # Create the bar chart
    fig, ax = plt.subplots()
    ax.bar(statuses, counts)
    
    # Adding labels and title (optional)
    ax.set_xlabel('Status')
    ax.set_ylabel('Counts')
    ax.set_title('Counts by Status')
    plt.show()

