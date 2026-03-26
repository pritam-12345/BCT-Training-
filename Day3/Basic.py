# print("hello Students")
# print("""This is
# written using
# python""")
#  a=10
#  print(a)
#  print(type(a))
#  <class 'int'>
#  print (type(b))
#  <class 'float'>
#  s='Hello World'
# # # Data Types:
# # # Numbers:int,float,complex,long
# # # String:stwe can make it in '' or " "
# # # List: []
# # # Tuple: ()
# # # Dictionary: {}
# # # Set: {}
# # #Operator:
# # #Arithmetic Operator: +,-,*,/,%,//,**
#  print (2*3)
#  print (6/2)
# # #Write a python program for swapping of two numbers withoiut using temp or third variable
#  a=10
#  b=20
#  a=a+b
#  b=a-b
#  a=a-b
#  print("a=",a)
#  print("b=",b)

#  n1=int(input("Enter first number: ")) 
#  n2=int(input("Enter second number: "))
#  int("Before swapping n1={} amd n2 ={}".format(n1,n2))
#  n1=n1+n2
#  n2=n1-n2
#  n1=n1-n2
#  print("After swapping n1={} and n2={}".format(n1,n2))ṇ

# # #Comparison Operator: ==,!=,>,<,>=,<=
#  print(a is b)
#  print(a is not b)

#  Conditional Statements:
#  if,elif,else
# if True:
#     print("if condition is true")
# else:
#     print("This is else block")
    
# #Write a python program for check eligible for casting vote or note and the age will be user input
# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")
    
# #Write a python program for check the input age is kids,child,teenagers or adults
# age = int(input("Enter your age: "))
# if 0<=age<=5:
#     print("You are a kid")
# elif 5<=age<=11:
#     print("You are a child")
# elif 12<=age<=19:
#     print("You are a teenager")
# else :
#     print("you are an adult")
  
    
# #Loop:-While loop and for loop 
# i=1
# while(True):
#     print(i)
#     i=i+1 
#     if i==11:
#Write a python program to sum of first 10 natural numbers
sum=0
n=int(input("Enter number of terms:\n"))
for i in range(1,n+1):
    sum+=i
print(f'sum is :{sum}')
#List(Elemnts can be modified)
l=[50,69,25,80,78]
print(l[1:4])
print(min[l])
print(max[l])
print(l.count(80))
print(len(l))
#1.append(99)
print(l)
l[0]=32
print(l)
l=[78,98,25,49,55.65]
for item in l:
    print(item,end=" ")
    
#Tuples(Elements are constant)
    tp(56,98,88.25,80,45)
    print(tp)
#Dictionary
marks={"A":85,"B":75,"X":90,"Y"=65}
print(marks)
print(marks["A"])
print(marks["X"]).

s={"Banana","Apple","Orange","Apple"}
print(s)
#Functions
def add():
    a=10
    b=15
    a=a+b 
    print("Addition is",a)
#Function Call
res=add(15,20)
print("addition is",res)
