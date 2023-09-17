'''12. If-else statements'''
if(9>44):
    print("yes")
else:
    print("no")

# x=int(input("enter your age"))
# if(x>18):      #1             #if type 19 than #1 is true it will execute and further will code will not run end of program.
#     print("take alcohol")
# elif(x==18):   #2             #if type 18 than #1 was false next #2 is true it will execute and further code will not run end of program.
#     print("you are lucky")
# else:
#     print("underage")
print("\n")


'''13. match'''
a=2                                
match a:                #check the value of a and run that case.
    case 1:
        print("case is 1")
    case 2:             #if there are 2 cases than above one will execute and exit.
        print("case is 2")
    case 2:
        print("case is 22")
    case 233:
        print("case is 233")
    case _:             #by default this run if no case executed above.
        print("case is default")
print("\n")


'''14. For loop'''
for i in range(11):  #range() function start from zero, now i value go from 0 to 11.
    print(i+1)

#for loop can use with list.
a=[1,34,55,66,44]
for item in a:
    print(item)
print("\n")


'''15. while loop'''
i=0
while(i<10):   #if this statement is true, the loop is continous
    print(i)
    i+=1
    if(i==5):
        continue  #on i is 5 don't execute cbelow code
    if(i==5 or i==6):
        break   #when i is 5 stop the loop
print("\n")


'''16. function'''
def printhello(one,two):  #one and two are arguments of function
    print("hello",one,two)
def printhi(one,two): 
    return "hello ",one,two

printhello(63,"soham")
printhello("sharma",44)
print(printhi(44,66))