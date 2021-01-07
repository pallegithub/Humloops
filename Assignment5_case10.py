def sum_count_reverse(n):
    count=0
    sum=0
    rev_num=0
    count=0
    while n>0:
        reminder=n%10
        sum = sum + reminder
        rev_num=rev_num*10+reminder
        n=n//10
        count = count+1
    print("Sum of the Digits in a given number is ",sum)
    print("Count==>",count)
    print("Reverse of the Number is==> ", rev_num)
number = int(input("Enter the number==>"))
sum_count_reverse(number)
