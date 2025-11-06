# this is a program to find whether the entered number is a prime number or not
num=int(input("Enter any number:"))
count=0
for i in range(1,num+1):
    if num%i==0:
        count=count+1
    else:
        pass
if count==2:
    print("the entered number is a prime number")
else:
    print("the entered number is not a prime number")

