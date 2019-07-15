import datetime
class person:
    def __init__(self,name, birth):
        self.speak ="Hello"
        self.walk = "walking away"
        self.name=name
        self.birth=birth
        
    def get_speak(self):
        return self.speak
    
    def get_walk(self):
        return self.walk
        
    def get_name(self):
        return self.name
    
    def get_birth(self):
        return self.birth
        
    
nam =input("Enter your name ")
bir =input('Enter a date in YYYY-MM-DD format ')
year, month, day = map(int, bir.split('-'))
bir = datetime.date(year, month, day)

Joshua = person(nam, bir)

print (Joshua.get_speak())
print ("I am", Joshua.get_name())
print ("my date of birth is", Joshua.get_birth())
print ("I am", Joshua.get_walk())

