i=1
while i==1:
    name = input("enter your name:")
    if name.isalpha():
        print(f"your name {name} has been stored")
        i=0
    else:
        print("please type a valid name")
