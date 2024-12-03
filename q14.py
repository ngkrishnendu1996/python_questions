#Write a Python function that counts the number of vowels and consonants in a given string.

def count_vowels_and_consonants(s):
    vowels = "aeiouAEIOU"  
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"  
    
    vowels_count = 0
    consonants_count = 0
    
    
    for char in s:
        if char in vowels:
            vowels_count += 1
        elif char in consonants:
            consonants_count += 1
    
    return vowels_count, consonants_count


s = input("Enter a string: ")
vowels_count, consonants_count = count_vowels_and_consonants(s)
print(f"Vowels: {vowels_count}, Consonants: {consonants_count}")

