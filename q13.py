#Given a list of numbers, write a Python function to return the second largest number in the list.


def sec_largest(n):
    n = list(set(n))  
    n.sort()  
    if len(n) < 2:
        return "No second largest element"
    return n[-2]  


n = list(map(int, input("Enter the numbers separated by spaces: ").split()))
print("Second largest number:", sec_largest(n))
  




                   


    
