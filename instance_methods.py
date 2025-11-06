# instance methods

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Hi ",self.name)
        print("Your marks are:",self.marks)
    def grade(self):
        if self.marks>=60:
            print("You got first grade")
        elif self.marks>=50:
            print("Ypu got second grade")
        elif self.marks>=35:
            print("You got third grade")
        else:
            print("You are failed")
n=int(input("Enter the number of students:"))
for i in range(n):
    name=input("Enter name:")
    marks=int(input("Enter marks:"))
    s=student(name,marks)
    s.display()
    s.grade()
    print()
