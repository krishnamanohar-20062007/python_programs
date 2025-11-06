# this is a program to print the list order of the given elements
my_dict={}
my_list=eval(input("Enter the list of numbers:"))
k=int(input("Enter values to be compared:"))
for i in range (k):
    val=chr(65+i)
    my_dict[val]=i
list2=[]

for i in range(len(my_list)-k+1):
    x=0
    for j in my_dict:
        my_dict[j]=my_list[i+x]
        x=x+1
    list1=list(my_dict.values())
    list2.append(max(list1))
print(list2)
