# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    #opening the file  
    with open("./story.txt", "r") as openingfile:
        read_file_content = openingfile.read()
    return read_file_content


def count_words():
    text = read_file_content("./story.txt")
    # dividing sentences into words
    split_text = text.split()
    
    #creating a dictionary to store the words 
    count = {}
    #looping through each word and counting each appearance  
    for word in split_text:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count
    
    
print(count_words())

