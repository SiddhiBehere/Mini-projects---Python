
# Mini Projects - Python

## 1. Bank Management System

MyBank is a simple banking application built using Python's Tkinter library. It provides basic functionalities such as user registration, login, deposit, withdrawal, and transfer of funds.

### Features
- **User Registration**: Users can register by providing their personal details such as username, age, gender, email, mobile number, password, and security question.
- **Login**: Registered users can log in using their email and password.
- **Forgot Password**: Users can retrieve their password by answering the security question.
- **Deposit**: Users can deposit funds into their account.
- **Withdrawal**: Users can withdraw funds from their account, provided they have sufficient balance.
- **Transfer**: Users can transfer funds to other registered users.

### Requirements
- Python 3.x
- Tkinter
- PIL (Python Imaging Library)

### Installation
1. Clone or download the repository to your local machine.
2. Ensure you have Python installed on your system.
3. Install Tkinter and PIL libraries if not already installed:

  pip install tk

  pip install pillow

4. Run the `MyBank.py` file to launch the application.

### Usage
1. Run the `MyBank.py` file.
2. If you are a new user, click on the "Register" button and fill in the required details.
3. If you are an existing user, click on the "Login" button and enter your credentials.
4. Once logged in, you can perform various banking operations such as deposit, withdrawal, and transfer.

### Note
- Ensure that the `img.png` file is present in the same directory as the `MyBank.py` file for the application to display the logo correctly.
- This application is intended for educational purposes and may lack certain security features found in production-grade banking applications.

## 2. Hotel Management System

This is a Python program for managing a hotel's billing and menu system using the Tkinter library for the graphical user interface (GUI) and SQLite for database management.

### Features:
- GUI for easy interaction.
- Menu selection for various categories: Veg, Non-Veg, Beverages, and Desserts.
- Automatic calculation of the total bill based on the selected menu items.
- Database storage of orders including customer ID, table number, selected dishes, total price, and timestamp.
- Display of table number, current time, and date.
- Error handling for invalid inputs.

### Usage:
1. Run the program.
2. Select menu items from each category (Veg, Non-Veg, Beverages, Desserts).
3. Enter the table number.
4. Click on the "Done" button to place the order.
5. The total price will be displayed along with a success message if the order is placed successfully.
6. Close the window when finished.

### Dependencies:
- Python 3.x
- Tkinter
- SQLite

### Installation:
1. Install Python.
2. Ensure Tkinter is installed, it is usually included with Python.
3. No additional installation required for SQLite as it is included with Python's standard library.

### How to Run:
1. Save the code in a file with a `.py` extension.
2. Run the file using a Python interpreter.


### Note:
Make sure to have proper permissions and dependencies installed before running the program.
