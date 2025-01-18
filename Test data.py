import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
import time

# Define database connection details
def get_connection():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-00A743O\\SQLEXPRESS;'  # Ensure double backslashes for escaping
        'DATABASE=Trial;'
        'Trusted_Connection=yes;'
    )

def fetch_and_plot():
    # Connect to SQL Server
    conn = get_connection()
    print("Connection successful!")

    # Create a cursor and execute query
    cursor = conn.cursor()
    query = "SELECT * FROM Data WHERE Time > '2025-01-17 08:59:18.000';"  # Replace with your SQL query
    cursor.execute(query)

    # Fetch all results and column names
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]  # Extract column names from the query result

    # Load data into a pandas DataFrame with column names
    df = pd.DataFrame.from_records(rows, columns=columns)

    # Ensure 'Price' and 'Time' columns are correctly typed
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')  # Convert Price to numeric
    df['Time'] = pd.to_datetime(df['Time'])  # Convert Time to datetime

    # Calculate Moving Average
    df['Moving_Avg20'] = df['Price'].rolling(window=20).mean()  # 20-point moving average
    df['Moving_Avg200'] = df['Price'].rolling(window=80).mean()  # 20-point moving average
    # Plot the data
    plt.figure(figsize=(15, 8))
    plt.plot(df['Time'], df['Price'], label='Original Price')
    plt.plot(df['Time'], df['Moving_Avg20'], color='r', label='Moving Average 20')
    plt.plot(df['Time'], df['Moving_Avg200'], color='black', label='Moving Average 80')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    plt.title('Price and Moving Average Over Time')
    plt.grid(True)
    plt.show()

    # Close connection
    conn.close()

# Run the function every 20 seconds

