'''Write a function that accepts two strings and returns the indices of all the occurrences
of the second string in the first string as a list. If the second string is not present in the
first string then it should return -1.'''

text = input("Enter first string : ")
pattern = input("Enter second string : ")

lt = len(text)
lp = len(pattern)

ans = []

for i in range(0,lt-lp+1):
    if pattern == text[i:i+lp]:
        ans.append(i)

print("Indices of occurences : ",end='')
print(ans)