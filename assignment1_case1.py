print("Student Progress Report App")
SR=input("Enter student Roll no==>")
SN=input("Enter Student Name==>")
Subject1=int(input("Enter marks of the Subject1==>"))
Subject2=int(input("Enter marks of the Subject2==>"))
Subject3=int(input("Enter marks of the Subject3==>"))
Subject4=int(input("Enter marks of the Subject4==>"))
Subject5=int(input("Enter marks of the Subject5==>"))
Subject6=int(input("Enter marks of the Subject6==>"))
Total=Subject1+Subject2+Subject3+Subject4+Subject5+Subject6
avg=int((Total)/6)
if (Subject1>=40 &Subject2>=40 & Subject3>=40 & Subject4>=40 &Subject5>=40 & Subject6>=40):
    if(avg>=80 and avg<=100):
        print("")
        print("Student Roll no:",SR)
        print("Student Name:",SN)
        print("Total Marks:",Total)
        print("Average Marks",avg)
        print("Grade: A")
        print("")
    elif(avg>=60&avg<79):
        print("")
        print("Student Roll no:",SR)
        print("Student Name:",SN)
        print("Total Marks:",Total)
        print("Average Marks",avg)
        print("Grade: B")
        print("")
    elif(avg>=50&avg<59):
        print("")
        print("Student Roll no:",SR)
        print("Student Name:",SN)
        print("Total Marks:",Total)
        print("Average Marks",avg)
        print("Grade: C")
        print("")
    elif(avg>=40&avg<49):
        print("")
        print("Student Roll no:",SR)
        print("Student Name:",SN)
        print("Total Marks:",Total)
        print("Average Marks",avg)
        print("Grade: D")
        print("")
    else:
        print("")
        print("Student Roll no:",SR)
        print("Student Name:",SN)
        print("Total Marks:",Total)
        print("Average Marks",avg)
        print("Grade: Promoted")
        print("")
else:
    print("Grade:Promoted")