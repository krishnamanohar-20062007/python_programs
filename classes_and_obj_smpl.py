#classes and objects
'''print(student.__doc__)

help(student)'''
'''class student:
    name="Abhinay"
    age=18
    marks=99
    def talk(self):
        print("My name is : ",self.name)
        print("My age is: ",self.age)
        print("My marks are: ",self.marks)
        
s=student()
s.talk()'''


class student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def talk(self):
        print(" student name: {}\n Rollno: {}\n Marks: {}".format(self.name,self.age,self.marks))
        
s=student("Abhinay",18,99)
s.talk()

s1=student("varun",18,89)
s1.talk()


'''class student:

    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def talk(self):
        print("My name is : ",self.name)
        print("My age is: ",self.age)
        print("My marks are: ",self.marks)
        
name=input("Enter the name:")
age=int(input("Enter the age:"))
marks=int(input("Enter the marks:"))
s=student(name,age,marks)
s.talk()'''

'''class Test:
    def __init__(self):
        print("Constructor execution")
    def m1(self):
        print("method execution")
t1=Test()
t2=Test()
t3=Test()
t1.m1()'''

