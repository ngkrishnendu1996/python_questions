#Write a program to find all unique permutations of a given string. For example, if the input is "ABC", the output should be:
# ABC
# ACB
# BAC
# BCA
# CAB
# CBA

from itertools import permutations
def uni_perm(st):
    per=permutations(st)
    return sorted(set(" ".join(p) for p in per))
    
st=input("Enter the string:")
result=uni_perm(st)
print(result)





