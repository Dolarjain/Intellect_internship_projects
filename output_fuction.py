# printing a string in python
print("we can print annything inside a print")

#allso we can store value in variable and then call the variable for print value 
age=26
print("i am dolar and my age is",age)

#here we are seprating the characters or data with any special symbol or character with the help of 'sep' keyword
print(1,2,3,4)
print(1,2,3,4,sep=' # ') # seprate with # where is comma
print(1,2,3,4,sep=' # ',end=' @ ') # seprate with # where is comma end with @ 

# .format{} method we use to format the string as per the order 
print("\n")
x='superman'  # calling x variable
print("this is {}".format(x)) # printing x variable with .formate{} method
# here we are trying to print one sentance using .format sequence
x='spiderman'
y='marvel cenematic universe'
print("i am {} from {}".format(x,y))
print("{1} is one of most famous super hero of {0} {2}".format(y,x,'thanks for riading')) # here we have formated value by index

# here we are printing datatypes of variable values with hep of type() function
age=23
print(type(age))
height=5.6
print(type(height))
c=3+7j
print(type(c))
print(age)

# this is dj and my age is 21
age=21
name='dj'
print("this is {} and my age is {}".format(name,age))

# this is manish ,sumit and dolar and our age is 22,24,25
n1="manish"
n2="sumit"
n3="dolar"

a1=22
a2=24
a3=25
print("this is {0},{1} and {2} our {4} {3} {5}".format(n1,n2,n3,a1,a2,a3))