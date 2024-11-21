#Write a program to implement a stack using a list. Include the following operations:

# push(item): Add an item to the stack.
# pop(): Remove the top item from the stack.
# peek(): Return the top item without removing it.
# is_empty(): Check if the stack is empty.

class Stack:
    def __init__(self):
        self.stack = []   #initialize

    def push(self,item):
        self.stack.append(item)
        print(f"pushed: {item}")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty.Nothing to pop")
            return None

    def peek(self):
        if not self.is_empty() :
            return self.stack[-1]
        else:
            print("Stack is empty.Nothing to peek")
            return None

    def is_empty(self):
        return len(self.stack)==0   

    def display(self):
        print("Stack:",self.stack)
  

if __name__ == "__main__":
    s = Stack()
    
    
    s.push(10)
    s.push(20)
    s.push(30)
    s.display()
    
    print("Peek:", s.peek())  
    
    print("Popped:", s.pop()) 
    s.display()
    
    print("Is stack empty?", s.is_empty())  
    
    s.pop()
    s.pop()
    s.display()
    print("Is stack empty?", s.is_empty())  
    s.pop()  
