import sqlite3

def add_expense(amount, category, date):
    try:
        # Connect to the SQLite database (or create if it doesn't exist)
        conn = sqlite3.connect('data/expenses.db')
        cursor = conn.cursor()

        # Create table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                            id INTEGER PRIMARY KEY,
                            amount REAL,
                            category TEXT,
                            date TEXT)''')

        # Insert expense data
        cursor.execute('''INSERT INTO expenses (amount, category, date)
                          VALUES (?, ?, ?)''', (amount, category, date))

        # Commit changes and close the connection
        conn.commit()
        conn.close()

        print(f"Expense of {amount} added under {category} on {date}.")
    except Exception as e:
        print(f"Error: {e}")
