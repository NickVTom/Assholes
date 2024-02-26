#read EXCEL
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

#piechart

def create_pie(file_path):

   fig=plt.figure()
   ax = fig.add_axes([0,0,1,1])
   ax.axis('equal')
   wb=pd.read_excel(file_path)
   a = wb.groupby('Status').Status.count()
   b = wb.Status.unique()
   ax.pie(a, labels=b, autopct='%1.1f%%')
   plt.show()

#barchart
   
def create_bar(file_path):
   fig=plt.figure()
   ax = fig.add_axes([0,0,1,1])
   ax.axis('equal')
   wb=pd.read_excel(file_path)
   a = wb.groupby('Status').Status.count()
   b = wb.Status.unique()
   ax.bar(a, labels=b, autopct='%1.1f%%')
   plt.show()