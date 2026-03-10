from colorama import Fore, Style

class Calculator_v0_2:
    def __init__(self, a , b):
        self.a = a
        self.b = b
        
    def multiply(self):
        result = self.a * self.b
        print("\n\nThe result of multiplication is: ",Fore.GREEN + str(result), Style.RESET_ALL)
    
    def divide(self):
        if self.b != 0:
            result = self.a / self.b
            print("The result of division is:", Fore.RED + str(result), Style.RESET_ALL)
        else:
            print("Error: Division by zero is not allowed.\n\n")
    
    def plus(self):
        result = self.a + self.b
        print("\n\nThe result of addition is: ", Fore.BLUE + str(result), Style.RESET_ALL)
        
    def minus(self):
        result = self.a - self.b
        print("\n\nThe result of subtraction is: ", Fore.MAGENTA + str(result), Style.RESET_ALL)
    
def main():
    start = 1
    
    while start == 1:
        a = float(input("Enter number a: "))
        b = float(input("\nEnter number b: "))
        
        calc = Calculator_v0_2(a,b)
        
        task = int(input("Enter the operation you want to perform (multiply = 0/divide = 1/plus = 2/minus = 3): "))
        
        if task == 0:
            calc.multiply()
        elif task == 1:
            calc.divide()
        elif task == 2:
            calc.plus()
        elif task == 3:
            calc.minus()
            
        start = int(input("\n\nDo you want to use agian this app? (turn app on=1/off=0)"))

main()
        
        