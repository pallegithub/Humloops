import csv 
f=open("emp.csv",'r') 
r=csv.reader(f) #returns csv reader object 
data=list(r) 
print("id,name,salary") 
for line in data: 
    if line[0]=='' or line[1]=='' or line[2]=='':
        print(line[0:])
     