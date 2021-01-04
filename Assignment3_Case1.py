list1 = []
l_list = int(input("Enter the lenth of the list==>"))
u_list = []
d_list = []
for x in range(l_list):
    e_list = input("Enter the elements of the list==>")
    list1.append(e_list)
for y in list1:
    if y not in d_list:
        u_list.append(y)
        d_list.append(y)
print("Unique_list",d_list)


