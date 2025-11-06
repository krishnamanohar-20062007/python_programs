#instance variable

'''class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        print("Inside the constructor:")
        print("Name: ",self.name)
        print("Roll No: ",self.rollno)
    def update(self,marks):
        self.marks=marks
        print("\n Inside the method")
        print(f" {self.name}'s Marks: ",self.marks)

s1=student("Abhi",2)
s1.update(91)

s1.name="Abhinay"
s1.update(89)
print(s1.name)'''

'''class Employee:
    def __init__(self,name,emp_id):
        self.name=name
        self.emp_id=emp_id
        self.salary=100000
        print(" constructor initialized:")
        print(self.__dict__)
    def remove_salary(self):
        del self.salary
        print("\n After deleting salary within class")
        print(self.__dict__)

e1=Employee("Abhinay",2)
del e1.emp_id
print("\n After deleting empid outside class")
print(e1.__dict__)
e1.remove_salary()

e2=Employee("chiru",17)'''

