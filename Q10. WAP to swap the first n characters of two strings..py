# WAP to swap the first n characters of two strings.

str1 = input("Please Enter First String : ")
str2 = input("Please Enter Second String : ")

n = int(input('How many character you want to swap: '))

x = str2[:n] + str1[n:]
y = str1[:n] + str2[n:]

print("Your first has become :- ", x)
print("Your second has become :- ", y)