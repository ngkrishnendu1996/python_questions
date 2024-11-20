# Write a Python function that takes a string as input and returns all possible permutations of the characters in the string. The permutations should be returned as a sorted list.

# Example:
# Input:
# "abc"

# Output:
# ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

from itertools import permutations
def pos_set(s):
    

    per=permutations(s)
    return ([" ".join(p) for p in per])
s="abc"
result=pos_set(s)
print(result)

    