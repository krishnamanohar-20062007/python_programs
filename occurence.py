#this is  a program to find the occurence of the numbers in a string
my_str=input("Enter the string: ")
my_list=[]
mydict={}
k=0
for i in my_str:
    if i in"0123456789":
        if i not in my_list:
            c=0
            for j in my_str:
                if i==j:
                    c=c+1
                else:
                    pass
            mydict[i]=c
            k=k+1
if k>0:
     for i in mydict:
        print("The occurance of ",i, "is ",mydict[i])
else:
    print("NO numbers found")
            
