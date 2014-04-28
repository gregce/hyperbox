###################
# 2014-04-47 -- 
# Reacquaint with basic python functionality.
# Review common concepts to ensure familiarity

#Import Modules Here
import sys

#Gather our test code in a main() function
def main():
    print 'Hellow World', sys.argv[1]
     
#Create a basic function for returning multiplied strings
def multiplystring(s, exclaim):
    #returns a multiplied string based on some input
    #result=s+s+s
    result=s*3
    #Both + and * are called "overloaded" operators because they mean different things for numbers vs. for strings (and other data types).
    
    if exclaim:
        result=result+'!!!'
    return result
    
def testpringf(s,s1):
    test = 'This is my string that %s, dont you like my %s' % (s,s1)
    #Python has a printf()-like facility to put together a string. 
    #The % operator takes a printf-type format string on the left 
    #(%d int, %s string, %f/%g floating point), and the matching values in 
    #a tuple on the right (a tuple is made of values separated by commas, typically grouped inside parenthesis):
    return test

def listbuild(listy,itemtoadd):
    listy.append(itemtoadd)
    return list

#listy = ['test1','test2']
#listbuild(listy,'test3')
#print listy

#One common pattern is to start a list a the empty list [], then use append() or extend() to add elements to it:

#Standard boilerplate to call main() function to begin 
#By doing the main check, you can have that code only execute when you want to run the module as a program and not have it execute when someone just wants to import your module and call your functions themselves.
if __name__ == '__main__':
    #main()
    #print multiplystring('Test',1)
    print testpringf('rocks','string')
    
    #Fun fact, Python checks code at runtime, not compile time.
    
    #One file of Python code is called a *module*. The file "binky.py" is also known as the module "binky". 
    #A module essentially contains variable definitions like, "x = 6" and "def foo()". 
    #Suppose the file "binky.py" contains a "def foo()". The fully qualified name of that foo function is "binky.foo". 
    
    #A method is like a function, but it runs "on" an object. 
    #If the variable s is a string, then the code s.lower() runs the lower() method on that string object and returns the result 
    #(this idea of a method running on an object is one of the basic ideas that make up Object Oriented Programming, OOP). 
    
    
    #Common String Methods
    
    #s.lower(), s.upper() -- returns the lowercase or uppercase version of the string
    #s.strip() -- returns a string with whitespace removed from the start and end
    #s.isalpha()/s.isdigit()/s.isspace()... -- tests if all the string chars are in the various character classes
    #s.startswith('other'), s.endswith('other') -- tests if the string starts or ends with the given other string
    #s.find('other') -- searches for the given other string (not a regular expression) within s, and returns the first index where it begins or -1 if not found
    #s.replace('old', 'new') -- returns a string where all occurrences of 'old' have been replaced by 'new'
    #s.split('delim') -- returns a list of substrings separated by the given delimiter. The delimiter is not a regular expression, it's just text. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. As a convenient special case s.split() (with no arguments) splits on all whitespace chars.
    #s.join(list) -- opposite of split(), joins the elements in the given list together using the string as the delimiter. e.g. '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc

    
    #Lists
    #Assignment with an = on lists does not make a copy. 
    #Instead, assignment makes the two variables point to the one list in memory.

    #b = colors   ## Does not copy the list
    
    #FOR operator for collections
    #Python's *for* and *in* constructs are extremely useful, and the first use of them we'll see is with lists. The *for* construct -- for var in list -- is an easy way to look at each element in a list (or other collection). 
    #Do not add or remove from the list during iteration.
   
    #Never manually iterate over a collection, use the FOR/IN construct in Python
    
    #for i in range(100) is one way to iterate, while i < NUMBER: i=i+1
    
    #Common list methods include
    
    #list = ['larry', 'curly', 'moe']
    #list.append('shemp')         ## append elem at end
    #list.insert(0, 'xxx')        ## insert elem at index 0
    #list.extend(['yyy', 'zzz'])  ## add list of elems at end
    #print list  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
    #print list.index('curly')    ## 2
    
    #list.remove('curly')         ## search and remove that element
    #list.pop(1)                  ## removes and returns 'larry'
    #print list  ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']
