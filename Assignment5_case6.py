def maximum(list): 
    max = list[0] 
    for i in list: 
        if i > max: 
             max=i
    return max
length=int(input("Enter the length of the list==>"))
list1=[]
for i in range(length):
    element=int(input("Enter the element==>"))
    list1.append(element)
print("")
print("Maximum Element==>", maximum(list1)) 