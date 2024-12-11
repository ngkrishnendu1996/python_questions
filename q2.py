#1,Given a list of strings, group the strings that are anagrams of each other. Return the result as a list of lists, where each sublist contains words that are anagrams of each other.


words = ["eat", "tea", "tan", "ate", "nat", "bat"]


anagrams = {}

for word in words:
    
    sorted_word = ''.join(sorted(word))
    
    
    if sorted_word in anagrams:
        anagrams[sorted_word].append(word)
        #print(f"==> {anagrams}")
    else:
        
        anagrams[sorted_word] = [word]


output = list(anagrams.values())
# print(anagrams)
print(output)
