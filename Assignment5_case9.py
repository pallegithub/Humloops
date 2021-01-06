def reverse(string):
	empty = ''
	i=len(string)-1
	while i>=0:
		empty=empty+str[i]
		i=i-1
	return empty
str=input("Inser the string===>")
print(reverse(str))
