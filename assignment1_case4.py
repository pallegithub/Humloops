#Power Consumption Calculator
while True:
    print("Power Consumption Calculator ")
    print("")
    pm=int(input("No. of units of power consumption==>"))
    if pm>=1 and pm<=50:
        print("")
        ba=pm*3
        print("UNITS==>",pm)
        print("Total Bill",ba)
        print("")
    elif pm>=51 and pm<=100:
        print("")
        ba=pm*6
        print("UNITS==>",pm)
        print("Total Bill",ba)
        print("")

    elif pm>=101 and pm<=150:
        print("")
        ba=pm*9
        print("UNITS==>",pm)
        print("Total Bill",ba)
        print("")
    elif pm>=151 and pm<=200:
        print("")
        ba=pm*12
        print("UNITS==>",pm)
        print("Total Bill",ba)
        print("")
    else:
        print("")
        ba=pm*15
        print("UNITS==>",pm)
        print("Total Bill",ba)
        print("")