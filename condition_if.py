#simple if deminstration
'''name=input("Enter Name:")
if name=='Abhinay':
    print("Hello Abhinay")
else:
    print("Hello guest")
print("How are you")'''

# write a program to find the biggest among 3 numbers

a,b,c=eval(input("Enter three numbers:"))
if(a>b and a>c):
    print('a is greater')
elif  b>c and b>a:                      
    print('b is greater')
else:
    print('c is greater')
