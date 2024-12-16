#Create a function to count the number of vowels in a string.
def count_vowels(input_string):
    count = 0
    vowels = "aeiou"
    for char in input_string:
        if char.lower() in vowels:
            count += 1
    return count

# Test the function
Str = "I am a Data scientist, works in a reputed firm"
vowel_count = count_vowels(Str)
print(f"The number of vowels in the string is: {vowel_count}")
