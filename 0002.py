def is_number():
    start = 1
    while start == 1:
        number = int(input("Enter a number: \n You can enter any number, but it must be an integer: "))
        if number % 2 == 0:
            print ("Even")
        else:        
            print ("Odd")
        start = int(input("Enter 1 to continue or 0 to stop: "))

is_number()