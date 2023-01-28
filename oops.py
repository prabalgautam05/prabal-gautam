class flat:
    def __init__(self,name,age,year):
        self.name= name
        self.age= age
        self.year= year
a= flat("naman",19,"1st year")
b= flat("chirag",18,"1st year")

print(a.__dict__,b.__dict__)
class partner(flat):
    def __init__(self,name,age,year,contact):
        self.name= name
        self.age= age
        self.year= year
        self.contact= contact
c= partner("shreyas","18","1st",100)
print(c.__dict__)

        