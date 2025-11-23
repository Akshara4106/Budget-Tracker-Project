Project Title : Python Command-Line Budget Tracker

Project Overview

This Python-based Budget Tracker addresses the challenge of managing personal finances effectively. It allows users to input income and categorize expenditures (eg: bills, groceries and other expenses) offering real-time financial summaries. The project applies foundational programming concepts to ensure data persistence and user-friendly management.

Structured Development Process

1 
Problem Definition :- (Identify a real-world problem)

*Problem:- The lack of a simple, automated system for individuals to track varying monthly income and categorize expenditures, often resulting in inaccurate budgeting.

*Goal:- To develop a functional, user-friendly command-line utility that provides instant, accurate financial reporting and promotes better personal money management.

2
Requirement Analysis:- (Define clear objectives)

Functional Requirement

*The application must allow users to **Add Income** (amount and source).
*The application must allow users to **Add Expenses** (amount, date, and        category).
*The application must display a **Summary Report** (Total Income, Total Expenses, Remaining Balance). 
*The application must use **File I/O** to save and load transactions from the `budget_data.json` file. 
*All user inputs must be validated to handle errors gracefully (e.g., preventing crashes from non-numeric input). 

3
Top-Down Design / Modularization

The project uses modular design with separate functions for clean code and easy testing:

* **`main_menu()`:** Controls the flow of the application and handles user choice routing.
* **`add_transaction(type)`:** Handles input gathering and validation for both income and expenses.
* **`calculate_balance()`:** Contains the primary logic to iterate through stored data and compute financial totals.
* **`data_persistence()`:** Manages reading and writing data to the persistent file (`budget_data.json`).

4
Algorithm Development

The core logic is based on simple arithmetic and conditional processing:

* **Data Structure:** All transactions are stored in a **List of Dictionaries** in Python, enabling easy categorization and calculation.
* **Core Balance Algorithm:**
    $$\text{Remaining Balance} = \sum_{\text{Income}} (\text{Amount}) - \sum_{\text{Expense}} (\text{Amount})$$

5
Implementation

* **Language:** Python 3.13.5
* **Tools/Libraries:** Standard Python Library 
* **Concepts Applied:** Functional Decomposition, Exception Handling (for input errors), File I/O for persistence, and basic Data Structure manipulation.

6
Testing and Refinement

The program was tested against several scenarios:

* **Test Case 1 (Persistence):** Verified that transactions added during one session are correctly loaded upon restarting the program.
* **Test Case 2 (Input Validation):** Tested entering letters and negative numbers; the program correctly handled the input and prompted the user for a valid entry.
* **Test Case 3 (Zero Balance):** Confirmed the summary correctly displays a zero balance when total income equals total expenses.



3
Submission and Access Details

Submission Details

1.  **Clone the Repository:** 'git clone https://github.com/Akshara4106/Budget-Tracker-Project.git'
2.  **Navigate to Directory:** `cd Budget-Tracker-Project`
3.  **Run the Script:** `python budget-tracker-project.py`

Visual Demonstration

* Screenshots of the program's output demonstrating its functionality (menu, data entry, summary) are provided in the **`/screenshots`** directory.

Licensing

This project is distributed under the **[MIT License](LICENSE)**.