'''9. Tuple and Tuple methods= in one variable store multiple values, values are called element.
                               we cannot change value, when we use () brackets than it is Tuple.'''
#it like string it cannot be changed too.
t1=(66,544,"sharma",6)
print(t1.count(544))
print(len(t1)) #total elemnts in tuple


'''10. set and set methods= collection of well defined objects, the elemnts not repeat in set and does not store values in order.'''
a={3,4,"soham",4,4,5}
b={65,55,55}
print(a) #output= {'soham', 3, 4, 5} this result keep on changing
print(type(a))
# print(a.pop()) #remove any random element from set.
print(a.union(b)) # print non common elements of both sets
print(a.union(b)) # print common elements of both sets.
print(len(a)) #output= 4, because repeated elemenst doesn't count.
# print(a[0:3])
#how to make empty set
c=set()
print(type(c))


'''11. dictionary and dictionary methods= it is key : value pair, it can muttable'''
d={"soham": "sharma", "sharma": 56, 66: "hello"}
s={}
print(type(s))
print(d)
print(d[66])
d[66]="soham" #key: value pair will add in the end of dictionary
print(d)
print(d.get("priyanka chopra")) #output= none, it is good than print(d[66])