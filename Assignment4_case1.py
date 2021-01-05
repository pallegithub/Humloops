dict = {}
while True:
 print("MY TO DO APP")
 print("===========")
 print("1. Add Task")
 print("2. View All Tasks")
 print("0. EXIT")
 option=int(input("PLEASE CHOOSE OPERATION"))
 if option==1 :
    print("")
    newkey1 = input("Enter the Task")
    value = input("Enter the Date")
    dict[newkey1] = value
    print("Task Added")
    print("")
 elif option==2:
    print("")
    print(dict)
    print("")
 elif option==0:
    print("Bye")
    break

 else:
    print("Please choose correct option")



 x=input("Do U want to continue (yes or no)")
 if x != 'yes':
    print("bye")
    break