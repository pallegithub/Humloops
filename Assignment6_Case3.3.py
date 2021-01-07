import csv 
f=open("emp.csv",'r') 
r=csv.reader(f) #returns csv reader object 
data=list(r) 
print("id,name,salary") 
for line in data: 
    if line[1][0]=='A':
        print(line[0:])
     