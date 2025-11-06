# method overloading // member function overloading
# only single method is used to overload
# done by using defaul arguments or variable length arguments


'''#default arguments
class demo:
    def greet(self,name=None):
        if name:
            print("Hello ",name)
        else:
            print("Hello")

d=demo()
d.greet()
d.greet("Abhi")'''
            

#variable length arguments

class calculator:
    def add(slef,*args):
        return sum(args)

c=calculator()
print(c.add(2))
print(c.add(1,2,3))

