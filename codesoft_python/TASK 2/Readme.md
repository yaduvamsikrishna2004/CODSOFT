Simple Calculator

A command-line calculator written in Python. This script allows users to perform basic arithmetic operations including addition, subtraction, multiplication, and division. It supports repeated calculations and handles errors such as division by zero and invalid inputs.
Features

    Addition: Adds two numbers.
    Subtraction: Subtracts one number from another.
    Multiplication: Multiplies two numbers.
    Division: Divides one number by another, with error handling for division by zero.
    Error Handling: Provides user-friendly messages for invalid inputs.
    Repeat Calculations: Allows users to perform multiple calculations in one session.

Getting Started
Prerequisites

    Python 3.x installed on your machine.


Run the script:

bash

    python calculator.py

Usage

When you run the script, you will be prompted to enter two numbers and choose an arithmetic operation. After displaying the result, the script will ask if you want to perform another calculation.
Example

text

Greetings! Let's perform some calculations together.

Enter the first number: 11
Enter the second number: 5

Choose an operation:
Enter (1) for Addition (+)
Enter (2) for Subtraction (-)
Enter (3) for Multiplication (*)
Enter (4) for Division (/)
Enter the value (1, 2, 3, 4) to choose the operation: 1
The result of 11.0 + 5.0 is: 16.0

Do you want to perform another calculation? (yes/no): no
Thank you for using the calculator. Goodbye!

Error Handling

    Invalid Numeric Input: If a non-numeric value is entered, the script will prompt the user to enter valid numeric values.
    Division by Zero: The script handles division by zero with an error message.