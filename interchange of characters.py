# this is a program to interchange the characters of a word
word=input("Enter any word you want:")
mylist=list(word)
char1=input("Enter the first character:")
char2=input("Enter the second character:")
new=""
for i in range(len(mylist)):
    if  mylist[i]==char1:
        mylist[i]=char2
    elif mylist[i]==char2:
        mylist[i]=char1
for i in mylist:
    new=new+i
print("the new word is ",new )
    
    
