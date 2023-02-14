from cmath import sqrt
print("THE QUADRATIC EQUATION IS IN THE FORM OF Ax^2+Bx+C")
A=float(input("enter the value of A="))
B=float(input("enter the value of B="))
C=float(input("enter the value of C="))
D=(B**2) + (4*A*C)
if D<0:
    print("roots dosn't exist")
    (exit())
    repeat(1)
if D>0:
    x=(-B+D)/(2*A)
    y=(-B-D)/(2*A)
print("the roots of the equation are {0} and {1}" .format(x,y))
