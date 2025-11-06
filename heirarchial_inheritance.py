# heirarchial inheritance

class a:
    def methodA(self):
        print("method A")
class b(a):
    def methodB(self):
        print("method B")
class c(a):
    def methodC(self):
        print("method C")

c1=b()
c2=c()
c1.methodA()
c1.methodB()
c2.methodC()
