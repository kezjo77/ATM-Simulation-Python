# ATM Simulation in Python

A simple command-line ATM simulation built using Python.
This project mimics basic ATM functionalities like checking balance, depositing money, and withdrawing cash, along with secure PIN input using masked characters.

# Features

*  PIN entry with masked input (`*`)
*  Real-time keypress handling (no need to press Enter)
*  Backspace support while entering PIN
*  Check account balance
*  Deposit money
*  Withdraw money
*  Loading animation for realistic ATM feel

# Technologies Used

* Python
* `msvcrt` (for real-time keyboard input - Windows only)
* `time` (for delay/animation)
* `random` (for generating account balance)

# How It Works
* The program generates a random account balance at runtime
* User selects an option:
  * Check Balance
  * Deposit
  * Withdraw
* Before processing, the user enters a PIN
* The PIN is masked with `*` for security
* The system processes the request and displays the result

# Notes
* This is a **simulation project** and does not store real data
* Account balance resets every time the program runs
* PIN is not validated (for demonstration purposes)
* Works only on **Windows** due to `msvcrt` module

# Future Improvements
* Add PIN validation system
* Limit PIN attempts
* Store balance using files or database
* Add transaction history
* Improve UI/UX

# Acknowledgment
This project was built as a learning exercise to understand:
* Python input handling
* Terminal control
* Basic program structure

Author
KEZIA JOSE