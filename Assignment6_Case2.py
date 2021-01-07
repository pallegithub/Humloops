while True:
 print("MY TO DO APP")
 print("===========")
 print("1. Add Task")
 print("2. View All Tasks")
 print("0. EXIT")
 option=int(input("PLEASE CHOOSE OPERATION==>"))
 if option==1 :
    task = input("Enter task name==>")
    file = open("mytasks.txt", "w")
    file.write('\n'+ task + '\n')
    file.close()
    print("Task Added")
 elif option==2:
    print("Task List")
    file = open("mytasks.txt", "r")
    data=file.read()
    print(data)
    print() 
    file.close()  
 elif option==0:
    print("Bye")
    break
 else:
    print("Please choose correct option==>")


 x=input("Do U want to continue (yes or no)==>")
 if x != 'yes':
    print("bye")
    break