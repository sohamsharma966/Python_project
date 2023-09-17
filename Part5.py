'''17. try exception error'''

#what if user entered string value
# try: #so we can do try
#     a=int(input("enter your name ")) 
#     print(a+4)
# except Exception as e:   #if you want to see the error you can do exception as e and print e.
#     print("some error occured",e)
# print("\n")


'''18. how to handle file I/O'''
s="this is string"  
#you want to right this string in file

# with open("test.txt","w") as f:  #create file #with and as f is context manager is easy and you don't need to close it.
#     f.write(s) #put s string in file
#or
# fp= open("test.txt","w")
# fp.write(s)
# fp.close()


'''19. OOPS object oriented programming= talk about classes , objects, methods and properties.'''
#class= it is like a template, which is use to make a object. it is mpty form.
#object= it is filled form.

class employee: #empty form
    def __init__(self,name,salary):  #constructor function run automatically
        self.name=name               #whenever create function in class self argument is automatically pass, slef is refrence of that object.
        self.salary=salary
    def getsalary(self):
        print(self.salary)
    
rohan=employee("rohan","45000") #filled form
print(rohan.name)
print(rohan.salary)
rohan.getsalary()