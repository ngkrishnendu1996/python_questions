#Given an array containing n distinct numbers taken from the range 1 to n+1, find the one number that is missing from the array.Input: 
# [3, 7, 1, 2, 8, 4, 5]
#Output: 6
def find_missing_number(nums):
    n = len(nums)
    
    total_sum = (n + 1) * (n + 2) // 2
    
    array_sum = sum(nums)
   
    return total_sum - array_sum


nums = [3, 7, 1, 2, 8, 4, 5]
print(find_missing_number(nums))  # Output: 6
