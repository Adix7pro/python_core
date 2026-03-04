def avarage_of_numbers():
    numbers = []
    length = int(input("how many numbers do you want to enter?"))
    for i in range(length):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)
    print("This is unsorted list : ", numbers)
    avarage = sum(numbers) / length
    print("The avarage of the numbers is: ", avarage)
avarage_of_numbers()