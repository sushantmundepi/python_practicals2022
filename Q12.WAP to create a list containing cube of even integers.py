'''wap to create a list containing cubes of only even integers
appearing in the input . (a).(using for loops) (b)list comprehension'''
# (a) using loops
test = []
n = int(input('enter the length of list \n'))
for j in range(0, n):
    val = input('enter the values: ')
    test.append(val)
cubes = []
for i in test:
    if str(i).isdigit():
        if int(i) % 2 == 0:
            i = int(int(i) ** 3)
            cubes.append(i)
print('The cubed values of all the even digits in the given string using for loop are: ')
print(cubes)
# b)
list_comp = [int(cube)**3 for cube in test if cube.isdigit() and int(cube) % 2 == 0]
print('The cubed values of all the even digits in the given string using list comprehension are: ')
print(list_comp)



