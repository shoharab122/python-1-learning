def calculator():
    print("Welcome to the Python Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Take the operation input
    operation = input("Enter the number of the operation (1/2/3/4): ")
    
    # Validate the operation
    if operation not in ['1', '2', '3', '4']:
        print("Invalid operation. Please choose a valid option.")
        return
    
    # Take input numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    
    # Perform the operation
    if operation == '1':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}.")
    elif operation == '2':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}.")
    elif operation == '3':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}.")
    elif operation == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}.")
    
    # Ask if the user wants to perform another calculation
    again = input("Do you want to perform another calculation? (yes/no): ").lower()
    if again == 'yes':
        calculator()
    else:
        print("Thank you for using the calculator. Goodbye!")

# Run the calculator
calculator()




