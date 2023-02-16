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
        r1 = (-b-cmath.sqrt(d))/(2*a)
        r2 = (-b+cmath.sqrt(d))/(2*a)
        print('The solution are' , (r1,r2))
        break
    elif d==0 :
        r=-b/2*a
        print("both the roots are same" , r)
    else :
        print("no real roots")
        break
