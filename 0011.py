def main():
    start = 1
    while start == 1:
        operation = int(input("Enter the operation you want to perform (multiply = 1/divide = 0): "))
        if operation == 1:
            multiply()
        elif operation == 0:
            divide()
        else:
            print("Invalid operation. Please enter 1 or 0.")
        
        start = int(input("\nDo you want to start again? (1 for start again, 0 for stop)"))




def multiply():
    a = float(input("Enter a number: "))
    b = float(input("\nEnter another number: "))
    result = a * b
    print("\n\nThe result of multiplication is: ", result)

def divide():
    a = float(input("Enter a number: "))
    b = float(input("\nEnter another number: "))
    if b != 0:
        result = a / b
        print("The result of division is:", result)
    else:
        print("Error: Division by zero is not allowed.\n\n")


main()
