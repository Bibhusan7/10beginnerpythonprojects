#beginner calculator
while True:#running a while loop so that the calculator will the close until you want it to.
    print("""
    Choices.
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Remainder
    6. Power
    0. Exit
    """)
    choice = int(input("Enter your choice: ")) #getting users choice

    if choice == 1:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 + num2
        print(result)
    elif choice == 2:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 - num2
        print(result)
    elif choice == 3:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 * num2
        print(result)
    elif choice == 4:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 / num2
        print(result)
    elif choice == 5:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 % num2
        print(result)
    elif choice == 6:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 ** num2
        print(result)
    elif choice == 0:
        break
    else:
        print("No option.")
        break