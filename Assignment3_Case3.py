
list = []
total = 0
average = 0
for i in range(6):
    marks=int(input("Enter marks of each subject==>"))
    list.append(marks)
    total = total + marks
print("")
print("Marks of all the subjects==>")
print(list)
average = total / 6
print("Total marks==>",total)
print("Average==>",average)

