# multilevel inheritance

class a:
    def methodA(self):
        print("method A")
class b(a):
    def methodB(self):
        print("method B")
class c(b):
    def methodC(self):
        print("method C")

c1=c()
c1.methodA()
c1.methodB()
c1.methodC()
