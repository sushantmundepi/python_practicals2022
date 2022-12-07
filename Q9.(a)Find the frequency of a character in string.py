 #Finding the frequency of a character in a string.

from collections import Counter

test_str = "testing string"


res = Counter(test_str)


print ("Count of all characters in ", test_str, "is :\n "+ str(res))