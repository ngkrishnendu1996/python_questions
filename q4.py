#Write a function that takes a string as input and returns a compressed version of the string. If the compressed string is not shorter than the original, return the original. For example:

#Input: "aabcccccaaa"
#Output: "a2b1c5a3"

def compress_string(input_str):
    new_str = []
    count = 1  
    i = 0

  
    while i < len(input_str) - 1:
        if input_str[i] == input_str[i + 1]:  
            count += 1  
        else:
            new_str.append(input_str[i] + str(count))  
            count = 1  
        i += 1  

    
    new_str.append(input_str[i] + str(count))

    
    compressed = ''.join(new_str)

    
    return compressed if len(compressed) < len(input_str) else input_str



input_str = "aabcccccaaa"
print(compress_string(input_str))  
