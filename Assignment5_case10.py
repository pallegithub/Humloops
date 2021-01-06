def sum(n):
    if n==0:
        return n
    else:
        return (n%10)+sum(n//10)

def reverse(n): 
    r = 0
    while (n != 0): 
        r = r * 10
        r = r + n % 10
        n = n // 10
        return (r)
def operation(n): 
    a=sum(n)
    b=reverse(n)
number=int(input("Enter the number==>"))
operation(number) 

