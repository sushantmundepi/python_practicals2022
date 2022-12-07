# Remove the first occurrence of a character from a string.
my_str = 'apple'


def remove_first_occurrence(string, char):
    idx = string.index(char)

    return string[:idx] + string[idx+len(char):]


print(remove_first_occurrence('apple', 'p'))

print(remove_first_occurrence('abc one abc two', 'abc '))