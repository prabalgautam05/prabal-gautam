a=int(input("enter any number: "))
for i in range(a):
    for j in range(i+1):
        print("* ", end= "")
    print("\n")
for i in range (a,0,-1):
    for j in range(0,i-1):
         print("* ", end= "")
    print("\n")