# Owner: ceccarelli@
# Updated Date: 10/8/2014
# Purpose:
# 

# Buganizer:
# References:

"""To-Dos

1. Open the file to string
2. Parse the file -- 
   - Do we need to build a grammar?
   - Regex expressions?
   - Built in string manipulation functions?
3. For the initial example, persist as either a dictionary or pandas dataframe
4. Learn how to to connect to cloud sql
5. Test calling the changeling service directly

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""
import os
os.chdir('/Users/ceccarelli/Desktop')

filename = 'GSX Contract Output.txt'

def lower(word):
    return word.lower()

def create_dict(filename):
    #initialize a dictionary
    dictionary={}
    
    #open the specificed file
    re = open(filename,'r')
    
    #iterate over the lines in the file
    for line in re:
        #iterate over the words in the line
        for word in line.split():
            #check to see if the word is in the dictionary; if not, add it
            if lower(word) not in dictionary:
                dictionary[lower(word)] = 1
            #if key exists, update its count value
            else:
                count=dictionary.get(lower(word))+1
                dictionary[lower(word)]=count
                
    #close the file
    re.close()
    return dictionary

def read_all(filename):
    ra = open(filename,'r')
    
    for line in ra:
        print line
    return


#read_all(filename)

dictionary=create_dict(filename)
print dictionary['this']
dictionary.viewitems()
#for k, v in dictionary.items(): print k, v
print __file__