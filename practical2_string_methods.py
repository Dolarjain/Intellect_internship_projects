# defining strings in python
my_string='HELLO'
str2="Hello"
str3='''HELLO'''
str4="""hello
world"""
print(my_string)
print(str2)
print(str3)
print(str4)

# accessing string character in python

str="programers"
print('str=', str)

#first character accessing 
print("str[0]=",str[0])

#last character assessing
print('''str[-1]=''',str[-1])

#slicing perticular substring fron string
print('str[1:6]=',str[1:6])

#slicing 6th to 2nd last character
print('str[5:-2]=',str[5:-2])

# # index must be in range
print(str[15])

# #index must be integer
 print(str[1.5])

#str object does not support item assiangment 
my_string1='programing'
my_string[4]='d'

#we are changinh a string 
my_string1='python'
print(my_string1)
# we cant delete the item of string
del my_string1[2]

# deletion of str
del my_string1
print(my_string1)

#concatenation of strings
str1="john"
str2="wick"

# with the hepl of + oprator
print(str1+str2)

#using * we can replicate the string 
print(str1*5)

#membeShip checking methods

print('a' in "dolar")
print('ar' not in "dolar")

# format method 
name = "dolar"
surname = "jain"
age = 21

print(" MY NAME IS {} {} AND MY AGE IS {}".format(name,surname,age))
print("\n")
print(" MY NAME IS {0} {2} AND MY AGE IS {1}".format(name,age,surname))
print("\n")
print(" MY NAME IS {n} {s} AND MY AGE IS {a}".format(n="dj",a="22",s="paddhariya"))

#common python string methods 
my_name="DolarJain"
print(my_name)
print(my_name.upper())
print(my_name.lower())
print(my_name.isupper())
print(my_name.islower())

# .split() do seprate every word and create a list of words 
print("my name is dolar and i will teach you python".split())
print(' '.join(['my', 'name', 'is', 'dolar', 'and', 'i', 'will', 'teach', 'you', 'java']))

# this fuction help us to find perticular string or substring is present or not in that string
print("welcome to jumanji".find('manji'))

#replace fuction use to replace any word with another word in string 
print("my friend is ashitosh".replace('ashitosh',"hitendra"))



