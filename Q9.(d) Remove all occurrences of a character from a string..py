# Remove all occurrences of a character from a string.

test_str = "GeeksforGeeks"

rem_char = "e"

print("The original string is : " + str(test_str))

new_str = ""
for i in test_str:
	if(i != rem_char):
		new_str += i
res = new_str
print("The string after character deletion : " + str(res))