class Student:
    def __init__(self,param1,param2): 
        self.name = param1
        self.gpa = param2
    def __str__(self):
        return '{} has {}'.format(self.name,self.gpa)
