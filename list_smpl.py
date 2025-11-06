# nested list and list traversals and list slicing

'''l=[10,20,[10,65]]
l1=l.copy()
l[2]=45
print(l)
print(l1[:100])'''


n=[1,2,3,4,5,6,7,8,9,10]
'''print(n[2:7:2])
print(n[4::2])
print(n[3:7])
print(n[8:2:-2])
print(n[4:100])'''

'''i=0
while i<len(n):
    print(n[i],end=' ')
    i=i+1
print()
for i in n:
    print(i)'''
n=[1,2,2,2,2,3,3]
n2=[1,433,123]
'''print(n.count(1))
print(n.count(2))
print(n.count(3))
print(n.count(4))'''

'''n1=[]
n.sort()
for i in range(len(n)):
    n1.append(n[i])
    i=i+(n.count(n[i]))
print(n1)'''

try:
    print(n.index(1))
    print(n.index(2))
    print(n.index(3))
    print(n.remove(100))
    print(n.index(4))
except ValueError:
    print("The value is not present ")
except IndexError:
    print("index out of range")

'''for i in range(1,5):
    if i in n:
        print(n.index(i))
    else:
        print("the value ",i,"is not present in the list")'''

n.insert(100,47)
print(n)
n.extend(n2)
n.append("asbdjhnsah")
print(n)

    


