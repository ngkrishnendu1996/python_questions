#Write a function group_anagrams that takes a list of strings as input and groups the strings that are anagrams of each other. The function should return a list of lists, where each sublist contains strings that are anagrams of each other.
words = ["listen", "silent", "enlist", "rat", "tar", "art", "cat", "act"]

anagrams={}

for word in words:
    sorted_words="".join(sorted(word))

    if sorted_words in anagrams:
        anagrams[sorted_words].append(word)
        #print(anagrams)
    else:
        anagrams[sorted_words] =[word]  


output=list(anagrams.values())    
print(output)