# heirarchial inheritance

class a:
    def methodA(self):
        print("method A")
class b(a):
    def methodB(self):
        print("method B")
class c:
    def methodC(self):
        print("method C")
class d(b,c):
    def methodD(self):
        print("method D")

d1=d()
d1.methodA()
d1.methodB()
d1.methodC()
d1.methodD()
