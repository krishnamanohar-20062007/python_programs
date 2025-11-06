'''#operator overloading
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return point(self.x+other.x,self.y+other.y)
    def __str__(self):
        return f"({self.x},{self.y})" 

p1=point(1,2)
p2=point(3,4)
p3=point(0,0)
try:
    #print(p1+p2)
    print(p1)
except TypeError:
    print("Type error has occured")'''




class student:
    def __init__(self,name,rno):
        self.name=name
        self.rno=rno
    def __eq__(self,other):
        return self.rno==other.rno and self.name==other.name

s1=student("abhi",2)
s2=student("abhwoejfn",2)
print(s1==s2)
