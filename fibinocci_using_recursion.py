#Write a recursive function to calculate the n-th Fibonacci number.

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

n = 10  
result = fibonacci(n)
print(f"The {n}-th Fibonacci number is {result}.")