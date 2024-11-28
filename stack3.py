#Implement a stack that supports a min() function that returns the minimum element in the stack, in constant time.

class Minimum_stack:

    def __init__(self):
        self.stack = []
        self.stack_min=[]


    def push(self, value):
        self.stack.append(value)  
        if not self.stack_min or value <= self.stack_min[-1]:
             self.stack_min.append(value)  

    def pop(self):
        if not self.stack :
            return None
        value=self.stack.pop()
        if value ==self.stack_min[-1]:
            self.stack_min.pop()
        return value    
    
    def peek(self):  
        if not self.stack:
            return None
        return self.stack[-1]
    
    def min(self):
        if not self.stack:
            return None
        return self.stack_min[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
stack=Minimum_stack()
stack.push(3)
stack.push(5)
stack.push(11)
stack.push(2)

print(stack.min())
stack.pop()

print(stack.min())