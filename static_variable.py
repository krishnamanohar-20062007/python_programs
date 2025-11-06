# static variable

class Employee:
    x=0
    def __init__(self):
        Employee.x=Employee.x+1
    def show(self):
        print("Total obj:",self.x)
e1=Employee()
e2=Employee()
e1.show()


'''class Test:
    x=10
    def __init__(self):
        self.y=20
t1=Test()
t2=Test()
print("t1:",t1.x,t1.y)
print("t2:",t2.x,t2.y)
Test.x=888
t1.y=999
print("t1:",t1.x,t1.y)
print("t2:",t2.x,t2.y)'''


class student:
    clg_name="Aditya college"
    def __init__(self):
        student.clg_name="Aditya University"
    def show(self):
        print("College name:",studnent.clg_name)

    def 


        
