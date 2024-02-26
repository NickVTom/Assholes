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