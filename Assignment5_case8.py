def factorial(n):
    if n == 0:
        print("") 
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        print(result)
        return result
n=int(input("Enter the  number=======>"))
factorial(n)
