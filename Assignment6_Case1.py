file = open("file1.txt", "w")
file = open("file1.txt", "r")
lines = 0
words = 0
characters = 0
for line in file:
  line = line.strip("\n")
  word = line.split()
  lines = lines + 1
  words = words + len(word)
  characters = characters + len(line)

file.close()
print("")
print("No of Lines==",lines)
print("No of Words==",words)
print("No of Charactters==",characters)
print("")
