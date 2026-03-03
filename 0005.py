def increase_list():
    start = 1
    while start == 1:
        numbers = []
        length = int(input("how many numbers do you want to enter"))
        for i in range(length):
            num = float(input(f"Enter number {i+1}:"))
            numbers.append(num)
            numbers.sort()
        
        print(numbers)
        start = int(input("Do you want to start again? (1 for yes, 0 for no)"))
    
increase_list()