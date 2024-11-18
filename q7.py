# Product of Array Except Self Question: Given an array nums of n integers where n > 1, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# python

# Verify

# Open In Editor Edit Copy code Input: nums = [1, 2, 3, 4] Output: [24, 12, 8, 6]

nums=[1,2,3,4]
total_products=1
output=[]
for i in nums:
    total_products*=i  
for num in nums:
    output.append(total_products//num)    

print(output)          

