# multiple inheritance
class a:
    def methodA(self):
        print("Method A")
class b:
    def methodB(self):
        print("Method B")
class c(a,b):
    def methodC(self):
        print("Method C")
c1=c()
c1.methodA()
c1.methodB()
c1.methodC()
