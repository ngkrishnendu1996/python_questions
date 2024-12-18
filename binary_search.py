def binary_search(array, target):
   
    left, right = 0, len(array) - 1

    while left <= right:
        mid = left + (right - left) // 2  
        if array[mid] == target:
            return mid  
        elif array[mid] < target:
            left = mid + 1  
        else:
            right = mid - 1  

    return -1  




sorted_array = [2, 4, 7, 10, 15, 20, 25]
target = 15

result = binary_search(sorted_array, target)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")
