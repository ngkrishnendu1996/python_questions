#Write a Python function that takes a string as input and returns the longest substring without repeating characters.
def longest_unique_substring(s):
    char_index_map = {}
    start = 0  
    max_length = 0  
    longest_substr = ""  

    for end in range(len(s)):
        current_char = s[end]
        
      
        if current_char in char_index_map and char_index_map[current_char] >= start:
            start = char_index_map[current_char] + 1  
        
        char_index_map[current_char] = end
        
        
        current_length = end - start + 1
        if current_length > max_length:
            max_length = current_length
            longest_substr = s[start:end + 1]

    return longest_substr
s=input("Enter the string :")
print(longest_unique_substring(s))