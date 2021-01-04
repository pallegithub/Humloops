while True:
 print("MY CALCULATOR")
 print("===========")
 print("1. ADD")
 print("2. SUB")
 print("3. MUL")
 print("4. DIV")
 print("0. EXIT")
 option=int(input("PLEASE CHOOSE OPERATION"))
 if option==1 :
    Number1=int(input("Enter Number1:"))
    Number2=int(input("Enter Number2:"))
    addition = Number1+Number2
    print("Result: ",addition)
 elif option==2:
    Number1=int(input("Enter Number1:"))
    Number2=int(input("Enter Number2:"))
    subtraction = Number1-Number2
    print("Result: ",subtraction)
 elif option==3:
    Number1=int(input("Enter Number1:"))
    Number2=int(input("Enter Number2:"))
    multiplication = Number1*Number2
    print("Result: ",multiplication)
 elif option==4:
    Number1=int(input("Enter Number1:"))
    Number2=int(input("Enter Number2:"))
    division = Number1-Number2
    print("Result: ",division)
 elif option==0:
    print("Bye")
    break

 else:
    print("Please choose correct option")

 
 x=input("Do U want to continue (yes or no)")
 if x != 'yes':
    print("bye")
    break