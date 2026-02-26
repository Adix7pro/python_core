def max_number():
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    max_num = max(num1, num2, num3)
    print("This is first way \n    The maximum number is:", max_num)


def max_number_2():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    if num1 >= num2 and num1 >= num3:
        max_num = num1
    elif num2 >= num1 and num2 >= num3:
        max_num = num2
    else:
        max_num = num3
    print("This is second way \n    The maximum number is:", max_num)

def max_number_list():
    numbers = []
    length = int(input("How many numbers do you want to enter? "))
    for i in range(length):
        num = float(input(f"Enter number {i+1}: "))
        numbers.append(num)
    max_num = max(numbers)
    print("This is third way \n    The maximum number is:", max_num)

def max_number_list_2():
    numbers = []
    lenght = int(input("How many numbers do you want to enter? "))
    for i in range(lenght):
        num = float(input(f"Enter number {i+1}: "))
        numbers.append(num)
    while len(numbers) > 1: 
        if numbers[0] >= numbers[1]:
            max_num = numbers[0]
            numbers.remove(numbers[1])
        else:
            max_num = numbers[1]
            numbers.remove(numbers[0])
    print("This is fourth way \n    The maximum number is:", max_num)
        
        
max_number_list_2()