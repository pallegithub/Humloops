#Discount Calculator app 
while True:
    print("Discount Calculator App ")
    print("")
    pm=int(input("Enter Purchase amount==>"))
    if pm>=100 and pm<=1000:
        print("")
        print("Purchase amount==>",pm)
        print("Dicount==>0")
        print("Total Bill",pm)
        print("")
    elif pm>=1001 and pm<=2000:
        a=(pm/100)
        b=a*10
        c=pm-b
        tb=c
        print("")
        print("Purchase amount==>",pm)
        print("Dicount",b)
        print("Total Bill",tb)
        print("")

    elif pm>=2001 and pm<=3000:
        a=(pm/100)
        b=a*20
        c=pm-b
        tb=c
        print("")
        print("Purchase amount==>",pm)
        print("Dicount",b)
        print("Total Bill",tb)
        print("")
    else:
        a=(pm/100)
        b=a*25
        c=pm-b
        tb=c
        print("")
        print("Purchase amount==>",pm)
        print("Dicount",b)
        print("Total Bill",tb)
        print("")