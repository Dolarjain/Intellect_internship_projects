# stack data sturucture algorithm
''' oprations we can perform on stack is 
    1.isempty()
    2.push()
    3.pop
    4.display()
'''
class stack_oprations:
    
    def __init__(self,stack_initial):
        self.stack_initial=stack_initial
        print("-----> stack oprations <-----")

    def isempty(self):
        print("-----> Checking Stack is Empty or Not \n")
        if len(self.stack_initial)==0:
            print("-----> Stack is Empty...")
        else:
            print("-----> Stack is not Empty")   

    def push_element(self,element):
        self.element=element
        self.stack_initial.append(element)
        print("-----> successful Operation Push Element")

    def pop_element(self):
        self.stack_initial.pop()
        print("-----> successful Operation Pop Element")    

    def display_stack(self):
        print("-----> Values of Stack :")
        for i in self.stack_initial:
            print(i)           

values_of_stack=['one','two','three','four','five']        
sta=stack_oprations(values_of_stack)
sta.isempty()
sta.push_element("seven")
sta.display_stack()
sta.pop_element()
sta.display_stack()      