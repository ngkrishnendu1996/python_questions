#Write a Python function that takes two sorted lists and merges them into one sorted list.
arr=[40,32,13,445,98,10,5,3,6,67]
n=len(arr)
for i in range(n):
    for j in range(n-1):
        if arr[i]<arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
print(arr)