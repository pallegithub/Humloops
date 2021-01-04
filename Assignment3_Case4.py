task_list = []

while True:
 print("MY TO DO APP")
 print("===========")
 print("1. Add Task")
 print("2. View All Tasks")
 print("0. EXIT")
 option=int(input("PLEASE CHOOSE OPERATION==>"))
 if option==1 :
    task = input("Enter task name==>")
    task_list.append(task)
    print("Task Added")
 elif option==2:
    print("Task Name")
    print(task_list)   
 elif option==0:
    print("Bye")
    break
 else:
    print("Please choose correct option==>")


 x=input("Do U want to continue (yes or no)==>")
 if x != 'yes':
    print("bye")
    break