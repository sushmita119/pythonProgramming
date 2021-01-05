class student1():
    def __init__(self,name):
        self.name = name
        
    def name(self):
        print("Name : {}".format(self.name))

class student2():
    def __init__(self,name):
        self.name = name
        
    def name(self):
        print("Name : {}".format(self.name))
def details(obj):
    obj.name()
stu1 = student1("Sushmita")
stu2 = student2("Shresthaa")
details(stu1)
details(stu2)
