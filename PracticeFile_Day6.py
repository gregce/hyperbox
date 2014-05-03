###################
# 2014-05-03 -- 
# Continue to Reacquaint with basic python functionality.
# Review common concepts to ensure familiarity. Learn some new concepts for the list.sort() operator.

#Tupes; fixed group size of elements that are immutable (unlike lists)

tuple = (1, 2, 'hi')
print len(tuple)  ## 3
print tuple[2]    ## hi
#tuple[2] = 'bye'  ## NO, tuples cannot be changed
#tuple = (1, 2, 'bye')  ## this works

#creating a tuple is different than standard variable assignment, in that syntax 
#requires an extra comma to make sure to asign "tupleness"

#List comprehensions -- more advanced features which is nice for some cases
#A way to write a compact express that operates on a list and expands said list

    ## Select fruits containing 'a', change to upper case
    #fruits = ['apple', 'cherry', 'bannana', 'lemon']
    #afruits = [ s.upper() for s in fruits if 'a' in s ]
    ### ['APPLE', 'BANNANA']
    
#Lists =[]
#Tuples = (x,)
#Dicts = {}


 ## Can build up a dict by starting with the the empty dict {}
  ## and storing key/value pairs into the dict like this:
  ## dict[key] = value-for-that-key
  dict = {}
  dict['a'] = 'alpha'
  dict['g'] = 'gamma'
  dict['o'] = 'omega'


 ## Common case -- loop over the keys in sorted order,
  ## accessing each key/value
  #for key in sorted(dict.keys()):
  #  print key, dict[key]

#Strategy note: from a performance point of view, the dictionary is one of your 
#greatest tools, and you should use where you can as an easy way to organize data. 
#For example, you might read a log file where each line begins with an ip address, 
#and store the data into a dict using the ip address as the key, and the list of 
#lines where it appears as the value. Once you've read in the whole file, you
#can look up any ip address and instantly see its list of lines. The dictionary 
#takes in scattered data and make it into something coherent.

#Dict formatting is somewhat similar to string formatting...; the % operator works 
#conviently to substitute values from a dictionary into a string

  # hash = {}
  #hash['word'] = 'garfield'
  #hash['count'] = 42
  #s = 'I want %(count)d copies of %(word)s' % hash  # %d for int, %s for string
  ## 'I want 42 copies of garfield'
  
  
#  
#  The "del" operator does deletions. In the simplest case, it can remove the definition of a variable, as if that variable had not been defined. Del can also be used on list elements or slices to delete that part of the list and to delete entries from a dictionary.
#
#  var = 6
#  del var  # var no more!
#  
#  list = ['a', 'b', 'c', 'd']
#  del list[0]     ## Delete first element
#  del list[-2:]   ## Delete last two elements
#  print list      ## ['b']
#
#  dict = {'a':1, 'b':2, 'c':3}
#  del dict['b']   ## Delete 'b' entry
#  print dict      ## {'a':1, 'c':3}


Exercise Incremental Development

#Building a Python program, don't write the whole thing in one step. Instead identify just a first milestone, e.g.
#"well the first step is to extract the list of words." Write the code to get to that milestone, and 
#just print your data structures at that point, and then you can do a sys.exit(0) so the program does
#not run ahead into its not-done parts. Once the milestone code is working, you can work on code for the
#next milestone. Being able to look at the printout of your variables at one state can help you think about 
#how you need to transform those variables to get to the next state. Python is very quick with this pattern, 
#allowing you to make a little change and run the program to see how it works. Take advantage of that quick turnaround 
#to build your program in little steps.
#  