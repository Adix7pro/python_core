def decrease_list():
    start =  1
    while start == 1:
        numbers = []
        length = int(input("how many numbers do you want to enter? "))
        for i in range(length):
            num = float(input(f"Enter number {i +1}: "))
            numbers.append(num)
        print("This is unsorted list : ", numbers)
        for i in range(length):
            for j in range(i+1, length):
                if numbers[i]< numbers[j]:
                    numbers[i],numbers[j] = numbers[j], numbers[i]
        print("This is second way \n    The numbers in decreasing order are:", (numbers))
        start = int(input("Do you want to start again? (1 for start again, 0 for stop)"))
        
        
        
decrease_list()
