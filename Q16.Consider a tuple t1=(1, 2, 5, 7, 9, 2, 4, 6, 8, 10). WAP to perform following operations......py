'''Consider a tuple t1=(1, 2, 5, 7, 9, 2, 4, 6, 8, 10). WAP to perform following operations:
a. Print half the values of the tuple in one line and the other half in the next line.
b. Print another tuple whose values are even numbers in the given tuple.
c. Concatenate a tuple t2=(11,13,15) with t1.
d. Return maximum and minimum value from this tuple'''

t1=(1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

tp1=t1[:5]
tp2=t1[5:]
#(a) part...
print(tp1)

print(tp2)
#(b)part...
eventp = tuple()
for i in t1:
    if(i%2 == 0) :
        eventp = eventp + (i,)

print("Even tuple : ")
print(eventp)
#(c) part....
t2 = (11,13,15)
t1 = t1 + t2

print(t1)
#(d) part...
print("Max : {}".format(max(t1)))
print("Min : {}".format(min(t1)))