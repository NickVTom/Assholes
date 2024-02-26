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

   fig=plt.figure()
   ax = fig.add_axes([0,0,1,1])
   ax.axis('equal')
   wb=pd.read_csv('Book1.csv')
   a = wb.groupby('Status').Status.count()
   b = wb.Status.unique()
   ax.pie(a, labels=b, autopct='%1.1f%%')
   plt.show()

