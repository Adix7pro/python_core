class Avarage_no_Funck:
    def calculator():
        start = 1
        sumnumbers = 0
        
        while start == 1:
            leng = int(input("Enter the length of numbers: "))
            numbers = []
            for i in range(leng):
                a = float(input("Enter number {} :".format(i+1)))
                numbers.append(a)
            for i in range(len(numbers)):
                sumnumbers += numbers[i]
            
            result = sumnumbers / leng
            print("The avarage of numbers is: ", result)
            start = int(input("\n\n Do you want to use agian this app? (turn app on=1/off=0)"))
            
Avarage_no_Funck.calculator()
            