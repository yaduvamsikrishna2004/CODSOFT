def calculator():
    print("Greetings! Let's perform some calculations together.")
    while True:
        try:
            # Prompt the user to input two numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Prompt the user to choose an operation
            print("\nChoose an operation:")
            print("Enter (1) for Addition (+)")
            print("Enter (2) for Subtraction (-)")
            print("Enter (3) for Multiplication (*)")
            print("Enter (4) for Division (/)")
            operation = int(input("Enter the value (1, 2, 3, 4) to choose the operation: "))

            # Perform the calculation based on the user's choice
            if operation == 1:
                result = num1 + num2
                print(f"The result of {num1} + {num2} is: {result}")
            elif operation == 2:
                result = num1 - num2
                print(f"The result of {num1} - {num2} is: {result}")
            elif operation == 3:
                result = num1 * num2
                print(f"The result of {num1} * {num2} is: {result}")
            elif operation == 4:
                if num2 != 0:
                    result = num1 / num2
                    print(f"The result of {num1} / {num2} is: {result}")
                else:
                    print("Error: Division by zero is not allowed.")
            else:
                print("Invalid operation choice. Please choose a valid operation.")
        
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        
        # Ask the user if they want to perform another calculation:22
        continue_calculating = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if continue_calculating != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break

# Run the calculator function
calculator()
