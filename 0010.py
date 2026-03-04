def avarage_of_numbers():
    numbers = []
    start = 1
    while start == 1:
        sum = 0
        length = int(input("How many numbers do you want enter? "))
        for i in range(length):
            num = float(input(f"Enter number {i + 1}:  "))
            numbers.append(num)
        for i in range(len(numbers)):
            sum = sum + numbers[i]
            avarage = sum / length
        print("This is unsorted list : ", numbers,"\n\n\n")
        print("The avarage of the numbers is: ", avarage,"\n\n\n")
        start = int(input("Do you want to start again? (1 for start again, 0 for stop)"))
avarage_of_numbers()
