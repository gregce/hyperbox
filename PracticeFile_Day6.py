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