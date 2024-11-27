#Write a program to check if a string containing brackets is balanced. A string is considered balanced if every opening bracket has a corresponding closing bracket in the correct order.
def is_balanced(expression):
    stack=[]
    bracket={")" :"(","}":"{","]":"["}

    for brack in expression:
        
        if brack in bracket:
            if not stack:
                return "Not balanced"
            top=stack.pop()
            if bracket[brack]!=top:
                return "Not balanced"
        else:
            stack.append(brack)
              

    if stack:
        return "Not balanced"
    else:
        return "balanced"      
print(is_balanced("({[()]})")) 
print(is_balanced("({[})]"))      



