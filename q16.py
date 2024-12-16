#Write a function generate_parentheses(n) that takes an integer n and returns all combinations of well-formed parentheses with n pairs.

def generate_parentheses(n):
    def brackend(current,open_count,close_count):
        if len(current)== 2*n:
            result.append("".join(current))
            return

        if open_count<n:
            current.append("(")
            brackend(current,open_count+1,close_count) 
            current.pop() 

        if close_count<open_count:
            current.append(")")
            brackend(current,open_count,close_count+1)
            current.pop() 
            
    result=[] 
    brackend([],0,0) 
    return result     
n=3
print(generate_parentheses(n))    

