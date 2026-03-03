def increase_list():
    start = 1
    while start == 1:
        numbers = []
        length = int(input("How many numbers do you want to enter? "))
        for i in range(length):
            num = float(input(f"Enter number {i+1}: "))
            numbers.append(num)
        
        print("This is first way \n    The numbers in increasing order are:", (numbers))
        
        for i in range(len(numbers)):
            for j in range (i + 1, len(numbers)):
                if numbers[i] > numbers[j]:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
                
        print("This is second way \n    The numbers in increasing order are:", (numbers))
        
        start = int(input("Do you want to start again? (1 for yes, 0 for no)"))
        
increase_list()