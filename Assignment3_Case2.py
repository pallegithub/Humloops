# Vowels in a word
word = input("Enter a word==>")
list = ['a','e','i','o','u']
vowels = []
for i in range(len(word)):
    for j in range(len(list)):
        if word[i]==list[j]:
            vowels.append(word[i])

print(vowels)