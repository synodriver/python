import  requests
import  re
import parsel
class shcool:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def student(self):
        print(self.name,self.age)
a = shcool("刘华强","21")

print(a.name,a.age)
a.student()
