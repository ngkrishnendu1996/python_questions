#Given a list of integers, write a program to count how many times each element appears in the list. Return a dictionary with the counts.

# Example:
# Input: [1, 2, 2, 3, 3, 3]
# Output: {1: 1, 2: 2, 3: 3}

input= [1, 2, 2, 3, 3, 3,5,5,6]
dic={}
#count=0
for i in input:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]=dic[i]+1
       
print(dic)        






