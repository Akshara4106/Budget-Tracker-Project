import json
import os
from datetime import datetime

# Define the file name for persistence
DATA_FILE = 'budget_data.json'
transactions_list = []

def load_data():
    """Loads transactions from the JSON file."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except (IOError, json.JSONDecodeError):
            print("Error loading data file. Starting fresh.")
            return []
    return []

def save_data(data):
    """Saves current transactions to the JSON file."""
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)
        print("Data saved successfully.")
    except IOError:
        print("Error saving data.")

def get_valid_amount(prompt):
    """Handles input validation for transaction amount."""
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("Amount must be positive.")
                continue
            return amount
        except ValueError:
            print("Invalid input. Please enter a numerical amount.")

def add_transaction(transaction_type):
    """Adds a new Income or Expense transaction."""
    print(f"\n--- Add {transaction_type} ---")
    amount = get_valid_amount("Enter amount: ")
    category = input("Enter category (e.g., Salary, Groceries,Other expenses): ").strip()
    
    new_transaction = {
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'type': transaction_type,
        'category': category.title(),
        'amount': amount
    }
    transactions_list.append(new_transaction)
    print(f"{transaction_type} of ${amount:.2f} added to '{category.title()}' category.")

def calculate_summary():
    """Calculates and prints the current balance and spending by category."""
    if not transactions_list:
        print("\nNo transactions recorded yet.")
        return

    current_balance = 0.0
    spending_by_category = {}

    for t in transactions_list:
        amount = t['amount']
        category = t['category']
        
        if t['type'] == 'Income':
            current_balance += amount
        
        elif t['type'] == 'Expense':
            current_balance -= amount
            
            # Aggregate expense by category
            spending_by_category[category] = spending_by_category.get(category, 0) + amount
    
    # --- Reporting ---
    print("\n" + "="*40)
    print(f"💰 CURRENT BALANCE: ${current_balance:.2f}")
    print("="*40)
    
    if spending_by_category:
        print("\nSpending by Category:")
        # Sort for clean output
        sorted_spending = sorted(spending_by_category.items(), key=lambda item: item[1], reverse=True)
        for category, total in sorted_spending:
            print(f"  - {category}: ${total:.2f}")
    else:
        print("\nNo expenses recorded yet.")

def main_menu():
    """Displays the main menu and handles user input."""
    print("\n" + "--- Budget Tracker Menu ---".center(40))
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Summary")
    print("4. Save & Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        add_transaction('Income')
    elif choice == '2':
        add_transaction('Expense')
    elif choice == '3':
        calculate_summary()
    elif choice == '4':
        save_data(transactions_list)
        print("Thank you for using the Budget Tracker!")
        return True # Signal to exit
    else:
        print("Invalid choice. Please try again.")
    return False

# --- Main Program Execution ---
if __name__ == "__main__":
    transactions_list = load_data()
    exit_program = False
    
    while not exit_program:
        exit_program = main_menu()
        
