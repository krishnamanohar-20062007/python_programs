#constructor overloading through default members

class student:
    def __init__(self,name=None,age=None):
        self.name=name
        self.age=age
        if name and age:
            print("Name: ",name," Age: ",age)
        elif name:
            print("Name: ",name)
        else:
            print("No details")

s1=student()
s2=student("Abhi")
s3=student("Ravi",48)
