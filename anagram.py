# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
    
    #compare the length of both words
    if (len(word) == len(anagram)):
        
        #compare if both words are equal
        if (sorted(word) == sorted(anagram)):
            return True
        else:
            return False

