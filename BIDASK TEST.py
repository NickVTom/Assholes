import pyodbc
import requests
import time
from datetime import datetime

# Define database connection details
def get_connection():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-00A743O\SQLEXPRESS;'
        'DATABASE=Trial;'
        'Trusted_Connection=yes;'
    )

conn = get_connection()
print("Connection successful!")
conn.close()

# Function to fetch BTC price data from CoinGecko
def fetch_btc_prices():
    try:
        # Fetch BTC market price data
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
        response.raise_for_status()  # Raise an error if the request fails

        data = response.json()
        market_price = float(data['bitcoin']['usd'])

        # Approximate bid and ask using the market price
        price = market_price 
    

        return price
    except Exception as e:
        print(f"Error fetching BTC data: {e}")
        return None

# Function to insert bid, ask, and time into the database
def insert_btc_data():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Define the table name
        table_name = "Data"

        # Fetch the BTC bid and ask prices
        price = fetch_btc_prices()
        if price is None:
            return

        # Get the current time
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Construct and execute the INSERT query
        query = f"INSERT INTO {table_name} (price, Time) VALUES (?, ?);"
        cursor.execute(query, price, current_time)

        conn.commit()
        print(f"Inserted BTC data: Price={price}, Time={current_time}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    # Continuously fetch and insert BTC data every minute
    while True:
        insert_btc_data()
        time.sleep(60)  # Pause for 60 seconds