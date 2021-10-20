# Q1.create a class vehicle with max speed and mileage instance attributes.

print(" Welcome to class vehicle")

class vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
    def print_info(self):
        print("Max Speed of my bike is {} and mileage is {}".format(self.max_speed,self.mileage))
vehi=vehicle(120,65000)
vehi.print_info()           

# Q2. create a vehicle1 class without any variable and method.

print ("creating a class without any variable or method")
print("\n")
class vehicle1:
    print("now i am inside the class ")
veh=vehicle1()    

# Q3.create a class person use the __init__()function to assign values name and age.
class person:
    def __init__(self):
        self.name="dolar" 
        self.age=21
    def printmethod(self):

        print("my name is {} and my age is {}".format(self.name,self.age))
p1=person()
p1.printmethod()
print("\n")            
 


# Q4.insert a function that prints a greeting. and executes it on the p1 object.
class person:
    def __init__(self):
        self.name="dolar" 
        self.age=21
    def printmethod(self):

        print("my name is {} and my age is {}".format(self.name,self.age))
    def greate(self):
        print("greeting ")    
p1=person()
p1.printmethod()
print("\n")            
p1.greate() 
print("\n") 


# we can also call whatever we like as we can call self but it should be the first parameter of that method or constructor
# as follow i have created example
class person:
    def __init__(myoparameter):
        myoparameter.name="dolar" 
        myoparameter.age=21
    def printmethod(example_parameter):

        print("my name is {} and my age is {}   thank you".format(example_parameter.name,example_parameter.age))
    def greate(self):
        print("welcome ")    
p1=person()
p1.printmethod()
print("\n")            
p1.greate() 
print("\n") 