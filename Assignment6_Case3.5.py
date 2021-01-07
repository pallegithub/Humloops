import csv 
f=open("emp.csv",'r') 
r=csv.reader(f) #returns csv reader object 
data=list(r) 
for line in data: 
    if line[0]!='' and line[1]!='' and line[2]!='':
        print(line[0:])
     