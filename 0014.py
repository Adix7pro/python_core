class Avarage:
    # def __init__(self, numbers,lengt,a):
    #     self.numbers = numbers
    #     self.lengt = lengt
    #     self.a = a
    def calculator():
        start = 1
        
        while start == 1:
            lengt = int(input("Enter the length of numbers: "))
            numbers = []
            for i in range(lengt):
                a = float(input("Enter number {} :".format(i+1)))
                numbers.append(a)
                result = sum(numbers) / len(numbers)
            print("The avarage of numbers is: ", result)
            start = int(input("\n\nDo you want to use agian this app? (turn app on=1/off=0)"))
Avarage.calculator()

            