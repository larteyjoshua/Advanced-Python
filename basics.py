"""names = ["sam", "john", "james"]
print (map(len, names))

def sqr(x): return x ** 2
print(map(sqr, map(len,names)))

def too_old(x):
    return x > 30
ages = [22, 25, 29, 34, 56, 24, 12]
print(list(filter(too_old, ages)))"""

class person:
    def __init__(self,name, age):
        self.name=name
        self.age=age
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
nam =input("Enter your name")
ag = input("Enter your age")
Joshua = person(nam, ag)
print (Joshua.get_name() , Joshua.get_age(), "Years old")
        

