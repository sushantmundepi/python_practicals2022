#wap to make an upward pyramid

t= int(input("Enter the number of rows : "))
s = " "
d = "* "
n=t+1
m=1
for i in range(t):
  print(n*s,m*d)
  n -= 1
  m += 1
