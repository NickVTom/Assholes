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
    

def create_bar_chart(file_path, category_column, value_column, title=''):
    """
    Create and display a bar chart from Excel data.
    """
    import pandas as pd
    import matplotlib.pyplot as plt
    """""
    Parameters:
    - file_path: str, path to the Excel file.
    - category_column: str, name of the column containing category labels.
    - value_column: str, name of the column containing the values for each category.
    - title: str, title of the bar chart.
    """
    # Load the dataset
    data = pd.read_excel(file_path)
    
    # Plotting the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(data[category_column], data[value_column], color='skyblue')
    plt.xlabel(category_column)
    plt.ylabel(value_column)
    plt.title(title)
    plt.xticks(rotation=45)  # Rotate category labels for better readability
    plt.tight_layout()  # Adjust layout to not cut off labels
    plt.show()

