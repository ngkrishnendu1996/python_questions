#Write a Python function using the bubble sort algorithm to find the kth smallest element in a list. For example, given the list [7, 10, 4, 3, 20, 15] and k = 3, the function should return 7 (the 3rd smallest element).
arr=[7, 10, 4, 3, 20, 15]
k=3
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[i] < arr[j]:
            arr[i],arr[j]=arr[j],arr[i]


print(arr[k-1])            
    