#2,Given a string s, find the longest palindromic substring in s
#Input: "cbbd"
#Output: "bb"
def longest_palindromic(str):
    long=" "
    for i in range(len(str)):
        for j in range(i+1,len(str)+1):
            substring=str[i:j]
            if substring==substring[::-1] and len(substring)>len(long):
                long=substring
    return long 
c="cbbd"    
print(longest_palindromic(c))       


