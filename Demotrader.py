import pyodbc

# Define database connection details
def get_connection():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-00A743O\\SQLEXPRESS;'  # Ensure double backslashes for escaping
        'DATABASE=Trial;'
        'Trusted_Connection=yes;'
    )

# Fetch the latest BTC price from the Data table
def fetch_current_btc_price():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT price FROM Data WHERE id = (SELECT MAX(id) FROM Data);")
    result = cursor.fetchone()
    conn.close()
    
    if result:
        return result[0]
    return None

# Function to display balances
def show_balance(initial_balance_usd, btc_balance):
    print(f"Current USD balance: ${initial_balance_usd:.2f}")
    print(f"Current BTC balance: {btc_balance:.8f} BTC")  # Display up to 8 decimal places

# Function to buy BTC (allowing fractional BTC purchases)
def buy_btc(quantity, initial_balance_usd, btc_balance):
    current_btc_price = fetch_current_btc_price()
    
    if current_btc_price is None:
        print("Error: Could not fetch BTC price.")
        return initial_balance_usd, btc_balance
    
    total_cost = current_btc_price * quantity
    if initial_balance_usd >= total_cost:
        initial_balance_usd -= total_cost
        btc_balance += quantity
        
        # Optionally log transaction to 'transactions' table (if you need to)
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO transactions (quantity, purchase_price) VALUES (?, ?)",
                       (quantity, current_btc_price))
        conn.commit()
        conn.close()
        
        print(f"Successfully bought {quantity:.8f} BTC at ${current_btc_price} each for ${total_cost:.2f}.")
    else:
        print("Not enough USD to purchase this amount of BTC.")
    
    return initial_balance_usd, btc_balance

# Function to sell BTC (allowing fractional BTC sales)
def sell_btc(quantity, initial_balance_usd, btc_balance):
    if btc_balance >= quantity:
        current_btc_price = fetch_current_btc_price()
        
        if current_btc_price is None:
            print("Error: Could not fetch current BTC price.")
            return initial_balance_usd, btc_balance
        
        total_revenue = current_btc_price * quantity
        initial_balance_usd += total_revenue
        btc_balance -= quantity
        
        print(f"Successfully sold {quantity:.8f} BTC for ${total_revenue:.2f} at ${current_btc_price} each.")
    else:
        print("Not enough BTC to sell this amount.")
    
    return initial_balance_usd, btc_balance

# Main loop for user interaction
def main():
    initial_balance_usd = 1000000.00  # Start with $1000
    btc_balance = 0.0  # Start with 0 BTC
    
    while True:
        print("\nOptions:")
        print("1. Show balance (USD and BTC)")
        print("2. Show transaction history")
        print("3. Buy BTC")
        print("4. Sell BTC")
        print("5. Exit")
        
        choice = input("Select an option: ").strip()

        if choice == '1':
            show_balance(initial_balance_usd, btc_balance)
        elif choice == '2':
            print("\nTransaction History:")
            # Fetch transaction history (if available in 'transactions' table)
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT transaction_id, quantity, purchase_price, timestamp FROM transactions")
            transactions = cursor.fetchall()
            if transactions:
                for txn in transactions:
                    print(f"Transaction {txn[0]}: Bought {txn[1]:.8f} BTC at ${txn[2]} each on {txn[3]}")
            else:
                print("No transactions found.")
            conn.close()
        elif choice == '3':
            try:
                quantity = float(input("Enter the quantity of BTC to buy: ").strip())
                if quantity <= 0:
                    print("Please enter a positive quantity of BTC.")
                else:
                    initial_balance_usd, btc_balance = buy_btc(quantity, initial_balance_usd, btc_balance)
            except ValueError:
                print("Invalid input.")
        elif choice == '4':
            try:
                quantity = float(input("Enter the quantity of BTC to sell: ").strip())
                if quantity <= 0:
                    print("Please enter a positive quantity of BTC.")
                else:
                    initial_balance_usd, btc_balance = sell_btc(quantity, initial_balance_usd, btc_balance)
            except ValueError:
                print("Invalid input.")
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please select a valid number (1-5).")

if __name__ == "__main__":
    main()
