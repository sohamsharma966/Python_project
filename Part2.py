'''4. Pip and modules= in python we have pip from which we can install module which is a code written by others. to use that module do "import module_name"
Go to website > pandas.pydata.org > python packages are present on website.'''

#go to terminal.
#run "pip install pandas" to install & use.

#Use panadas module by "import pandas as pd" and "as" use to represent another name.

# import pandas as pd

# df=pd.read_excel()  #in () put location of file
# print(df)


'''5. String and string methods= string is not changeable'''
name="soham"
name='sharma' #strings work on single qoutes too.
print(name)
print(name[0:3]) #name[0:3]is string slicing operator #will get char0,1,2 only.| name[a:b] char print from a to b-1
print(name[1:4])
# name[0] = "h" #we cannot do this because we cannot change string
print(name[0:3]) #python has to make new string to print this.
#string methods
print(name.upper()) #call the methods of object string which is in name
print(name.capitalize())
print(f"his name is {name}")


'''6. User input method= we take input from user we use input method'''
# name1=input("Enter your name:") #when you use input metthod the value willl be string
# print(type(name1)) #type() is function 
# print(name1)
# print(int(name1)+1)#use typecasting
# print(type(name1)) #output= <class 'list'>


'''7. it is case sensitive language'''
hello=1
Hello=2
print(hello,Hello)
# another thing
a="hello"\
   "soham is a good boy" #\ use for multiple line string. (string show on one line)
b='hello'
c='''hello
soham is a good boy'''  #if we write = and then triple qoutes it will be count as string. it is good multiline string.(string show on multiple line)
print(a," and ",b," and ",c)


'''8. list and list methods= in one variable store multiple values, values are called element.
                             we can change when we use [] brackets than it is list.'''
l1=[3,5,687,"soham"]
print(type(l1)) #output= <class 'list'>
print(l1)
#string cannot be change but you can change list.
l1.remove("soham") #it will remove elemnt and it will modify this list, it will not create new create new data print like string
l1.sort()
print(l1)
l1.pop() #it will remove last element.
print(l1)
l1.append(72) #78 vlue will added to the end of the list
print(l1)
l1.extend([87,56,66]) #take existing list and extend it with extended list.
print(l1)
# l1.clear() # make list empty
print(l1)
print(l1[0:4])
