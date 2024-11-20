# Write a Python function that takes a list of integers as input and returns a list of all possible subsets (the power set) of the list. The subsets should be sorted in ascending order, and each subset itself should also be sorted in ascending order.

# Example:
# Input:
# [1, 2, 3]

# Output:
# [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

from itertools import combinations
 
def subset_num(ls):
    num.sort() 
    new_set=[]
      
    for i in range(len(ls)+1):
        for subset in combinations(num,i):
            new_set.append(list(subset)) 
    return new_set

num=[1, 2, 3]     
result=subset_num(num)
print(result)       