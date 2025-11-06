'''l=[10,10,20,50]
s={10,20,30}
print(s)

#mutable
#do not allow duplicate elements
# Order of insertion is not preserved
# represented in curly braces
#indexing is not possible
#empty curly braces is not a set
#mathematical operations like union , intersection etc are performed
#heterogeneous values are allowed
#set function can be used


#add function  adds only one element to the set
s.add(40)
print(s )

#update function - used to add multiple items to the set
#syntax of update ----  <set>.update(< iterable_objects >)
#iterable_objects------  like list,range,string ,tuple,etc....
s.update(l,range(5),(100,654,6465),(8498,651,351))
print(s)

#copy function---- returns copy of the set ,   it is cloned object

s1=s.copy()
print(s1)

#pop---- returns a random removed element from the set

print(s.pop())
s.pop()
print(s)
print(s1)

s2=set(l)
l=list(s2)
print(l)


#remove function()----- removes a specific element from the set and gives error if the element is not present in the set
s.remove(10)
print(s)
#discard function()----- removes a specific element from the set and does not give an error if the element is not present in the list
s.discard(100000)
print(s)


#clear function

s.clear()
print(s)
'''

#union func-----   <set1>.union(< set2 >) or  < set1 > | < set2 >

x={10,20,30}
y={30,40,50}
print(x.union(y))
print(x|y)

#intersection func-----   <set1>.intersection(< set2 >) or  < set1 > & < set2 >

x={10,20,30}
y={30,40,50}
print(x.intersection(y))
print(x&y)

#difference func-----   <set1>.difference(< set2 >) or  < set1 > - < set2 >

x={10,20,30}
y={30,40,50}
print(x.difference(y))
print(y-x)


#symmetric_difference func-----   <set1>.symmetric_difference(< set2 >) or  < set1 > ^ < set2 > ----- returns elements present in both the sets which are not common
x={10,20,30}
y={30,40,50}
print(x.symmetric_difference(y))
print(y^x)

print(len(x))
