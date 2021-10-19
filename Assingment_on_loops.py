#print first 10 natural numbers using while loop
print("printing 10 natural numbers using while loop")
i=1
while i<=10:
    print("----> ", i)
    i=i+1
print("out of loop\n")    

#print the following pattern
""" 1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
"""
print("-----> here i am printing pattern")

for i in range(6):
    for j in range(1,i+1):
        print(j,end=" ") 
    print("\n")
        
#print the following Star pattern
""" *
    * *
    * * *
    * * * *
    * * * * *
"""
print("-----> here i am printing Star pattern")

for i in range(6):
    for j in range(1,i+1):
        print("*",end=" ") 
    print("\n")
        
#calculate the sum of all numbers from 1 to a given number
num=(int(input("enter end number which you want:")))
sum=0
for i in range(num):
    print("sum= {} + {}".format(sum,i))
    sum=i+sum
print("\nsum of all numbers from 1 to {}= {}".format(num,sum))    
print("\n")

# write a program to print multiplication table of given number

mul=(int(input("Enter your Number for Multiplication Table:")))

for i in range(1,10+1):
    print(" {} X {} ={}".format(mul,i,mul*i))

print("")

#display numbers from a list using loops

list1=[22,33,23,44,23,55,75,88,99,34]
i=0
for x in list1:
    
    print("index {} of List = {}".format(i,x))
    i=i+1
print("end of list")

#print the following pattern
"""
   5 4 3 2 1
   4 3 2 1
   3 2 1 
   2 1
   1 
 
"""
print("\n")
print("i am printing number pattern:")
print("\n")
max=5
for i in range(1,6):
    for j in range(max,0,-1):
       print(j,end=" ")
    max=max-1 
    print("\n")    

#display numbers from -10 to -1 using for loop
print("printing numbers from -10 to -1 ")
for num in range(-10,0):
    print("\t ----->",num)

print("")    

print("----------> Thanks You <------------")