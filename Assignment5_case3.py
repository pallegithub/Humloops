def multiplication(num): 
    for i in range(1,11):
        print(num,"X",i,"=",num*i)
number = int(input("Enter any number==>"))
print("Multiplication Table for",number)
print("")
multiplication(number)
print("")