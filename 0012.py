class Calculator:
    def __init__(self, a , b):
        self.a = a
        self.b = b
        
    def multiply(self):
        result = self.a * self.b
        print("\n\nThe result of multiplication is: ", result)
    
    def divide(self):
        if self.b != 0:
            result = self.a / self.b
            print("The result of division is:", result)
        else:
            print("Error: Division by zero is not allowed.\n\n")
    
def main():
    start = 1
    while start == 1:
        a = float(input("Enter a number: "))
        b = float(input("\nEnter another number: "))
    
        calc = Calculator(a,b)
        operation = int(input("Enter the operation you want to perform (multiply = 1/divide = 0): "))
        if operation == 1:
            calc.multiply()
        elif operation == 0:
            calc.divide()
        else:
            print("Invalid operation. Please enter 1 or 0.")
            
        start = int(input("\nDo you want to start again? (1 for start again, 0 for stop)"))
   



main()