#Write a function to evaluate a postfix expression using a stack.
#Example input: 2 3 + 5 * → Output: 25.

def fixing(expression):
    stack=[]
    tokens=expression.split()
      
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            operand2=stack.pop() 
            operand1=stack.pop()

        if token== "+":
            stack.append(operand1 + operand2)
        elif token=="-":
            stack.append(operand1 - operand2) 
        elif token=="*":
            stack.append(operand1 * operand2)  
        elif token =="/":
            stack.append(operand1 / operand2) 
    return stack.pop()              









express="2 3 + 5 * "
result=fixing(express)
print(result)