import sqlite3

def delete_expense(amount, category, date):
    # Connect to the SQLite database
    conn = sqlite3.connect('data/expenses.db')
    cursor = conn.cursor()

    # Check if the expense exists
    cursor.execute("SELECT * FROM expenses WHERE amount = ? AND category = ? AND date = ?", (amount, category, date))
    expense = cursor.fetchone()

    if expense:
        # Delete the expense from the database
        cursor.execute("DELETE FROM expenses WHERE amount = ? AND category = ? AND date = ?", (amount, category, date))
        conn.commit()
        print(f"Expense of {amount} under {category} on {date} has been deleted.")
    else:
        print(f"No expense found for {amount} under {category} on {date}.")

    # Close the connection
    conn.close()

# Call the function to delete an expense
if __name__ == "__main__":
    delete_expense(100.0, 'Food', '2025-05-04')  # Example of calling the delete function
