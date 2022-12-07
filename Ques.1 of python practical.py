#python practical question 1
import cmath
a=int(input("enter coefficient for x^2 : "))
b=int(input("enter coefficient for x : "))
c=int(input("enter the constant term : "))
d = (b ** 2) - (4 * a * c)
print("discriminent = " , d)
while True :
    #for real roots
    if d>0 :
        d = (b**2) - (4*a*c)

        # find the two real solutions
        sol1 = (-b-cmath.sqrt(d))/(2*a)
        sol2 = (-b+cmath.sqrt(d))/(2*a)

        print('The solution are {0} and {1}'.format(sol1,sol2))

    elif d<0 :
        print("no real roots")
        break

