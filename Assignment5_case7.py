def tuple_min(tup):
    if len(tup) == 1:
        return tup[0]
    elif len(tup) >= 2:
        a = tup[0]
        b = tuple_min(tup[1:])
        return a if a<b else b
length=int(input("Enter the length of the tuple==>"))
list1=[]
tuple1=tuple(list1)
for i in range(length):
    element=int(input("Enter the element==>"))
    list1.append(element)
print("")
print("Minimum of the Elements in the tuple==>", tuple_min(tuple1)) 
print("")