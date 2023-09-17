# your first program in python.
print("hello world")

# comment out
'''multi line
   comment out'''

'''1. variables and built-in datatypes.'''
_num=1
#3num=2 #we can't use number at first in var.
num3=3
#%num=4 #we can't use % special char except _ at first in var.
print(_num)
print(num3)

a=5      #datatype= integer
print(a)
a=6.5    #datatype= float
print(a)
c= True  #datatype= boolean
print(c)
d="harry" #datatype= string, string is sequence of character
print(d)
e= None #datatype= none, that means nothing is there.
print(e)
#complex
#bytes
d={3,4,"soham",4,4,5}#datatype= {set} collection of well defined objects, the elemnts not repeat in set.
print(d)
l1=[3,5,687,"soham"] #datatype= [list] in one variable store multiple values, values are called element, we con change values.
print(l1)
t1=(354,255,"sharma",6) #datatype= (tuple) in one variable store multiple values, values are called element, we cannot change values.
#dictionary


'''2. typecasting concept= convert one datatype to another datatype'''
a="5"
#print(a+1) #it will not work because it is integer, you can run by converting string to integer.
print(int(a)+1) #convert a into integer and than add 1 to a.
b=5
print(b+1)


'''3. How operators work?'''
num1=4
num2=2
## Arithmetic operators= give result of adding value, substraction value etc using this operators. + - / // * % **
print("num1 + num2 is", num1+num2)
print("num1 - num2 is", num1-num2)
print("num1 * num2 is", num1*num2)
print("num1 / num2 is", num1/num2)
print("num1 // num2 is", num1//num2)
print("num1 ** num2 is", num1**num2)
print("num1 % num2 is", num1%num2)

## Assignment operators= assign value to variable using = with arithmetic operator. = =+ -= *= /= %=
a=4 #= is assignment operator which assign 4 to a
a+=2 #first + mean 2 add to a and then = mean reassign that value to a.
a-=2
a*=2
a/=2
a%=2
print(a)

## Comparisons operators= give result either True or False using this operators. < > 
x=4
y=3
print(x>y) #output= True
print(x<y) #output= False
print(x>=y) 
print(x<=y) 
print(x==y) #output= False
print(x!=y) #output= True
##-Logical operator= create logic with comparison operators. and or not
print(x==4 and x<y) #in and operator both need to be true than only output is true.
print(x==4 or x<y) #in or operator anyone is true than result is true
print(not(True)) #output= False

