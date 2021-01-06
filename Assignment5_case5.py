def max(num1,num2,num3): 
    if num1>=num2 and num1>=num3:
        print("Maximum of",num1,",",num2,",",num3,"is",num1)
    elif num2>=num1 and num2>=num3:
        print("Maximum of",num1,",",num2,",",num3,"is",num2)
    else:
        print("Maximum of",num1,",",num2,",",num3,"is",num3)
        
number1 = int(input("Enter Number1==>"))
number2 = int(input("Enter Number2==>"))
number3 = int(input("Enter Number3==>"))
print("")
max(number1,number2,number3)