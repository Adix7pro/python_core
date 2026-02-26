def min_number():
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    min_num = min(num1, num2, num3)
    print("This is first way \n    The minimum number is:", min_num)


def min_number_2():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    if num1 <= num2 and num1 <= num3:
        min_num = num1
    elif num2 <= num1 and num2 <= num3:
        min_num = num2
    else:
        min_num = num3
    print("This is second way \n    The minimum number is:", min_num)

def min_number_list():
    numbers = []
    length = int(input("How many numbers do you want to enter? "))
    for i in range(length):
        num = float(input(f"Enter number {i+1}: "))
        numbers.append(num)
    min_num = min(numbers)
    print("This is third way \n    The minimum number is:", min_num)

def min_number_list_2():
    numbers = []
    lenght = int(input("How many numbers do you want to enter? "))
    for i in range(lenght):
        num = float(input(f"Enter number {i+1}: "))
        numbers.append(num)
    while len(numbers) > 1: 
        if numbers[0] <= numbers[1]:
            min_num = numbers[0]
            numbers.remove(numbers[1])
        else:
            min_num = numbers[1]
            numbers.remove(numbers[0])
    print("This is fourth way \n    The minimum number is:", min_num)
        
        
min_number_list_2()