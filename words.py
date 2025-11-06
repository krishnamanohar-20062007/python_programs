#this is a program to print the words of a string
mystr=input("Enter the string: ")
words=mystr.split('a')
print(words)
print("The words are")
for i in words:
    print(i)
