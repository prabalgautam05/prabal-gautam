
a=int(input("enter any number: "))
if a>1:
    for i in range (2,int(a/2)+1):
        if (a % i) == 0:
            print(a,"is not prime number")
        break
    print ("The Prime Numbers in the range are: ")  
for a in range (0, a + 1):  
    if a > 1:  
        for i in range (2, a):  
            if (a % i) == 0:  
                break  
        else:  
            print (a)
