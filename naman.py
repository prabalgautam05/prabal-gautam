from cmath import sqrt
print ("general qradratic equation is Ax**2+Bx=C ")
A=float(input("enter value of A="))
B=float(input("enter value of B="))
C=float(input("enter value of C="))
D = (B**2)-(4*A*C)
if D < 0:
    print("roots are imaginary")
    (exit)
    
if D > 0:
    print("roots are real")
    X= (-B -D)/(2*A)
    Y= (-B +D)/(2*A)
    print('The solution are {0} and {1}'.format(X,Y))   
if D == 0:
    print("roots are real")
    D = sqrt(D)
    X= (-B -D)/(2*A)
    Y= (-B +D)/(2*A)
    print('The solution are {0} and {1}'.format(X,Y))   
     