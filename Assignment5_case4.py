def max(num1,num2): 
    if num1>num2:
        print("Maximum of",num1,",",num2,"is",num1)
    else:
        print("Maximum of",num1,",",num2,"is",num2)
number1 = int(input("Enter Number1==>"))
number2 = int(input("Enter Number2==>"))
print("The maximum of two Numbers is")
max(number1,number2)