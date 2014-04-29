###################
# 2014-04-28 -- 
# Continue to Reacquaint with basic python functionality.
# Review common concepts to ensure familiarity. Learn some new concepts for the list.sort() operator.


#Key Functions
#Starting with Python 2.4, both list.sort() and sorted() added a key parameter to specify a function to be called on each list element prior to making comparisons.
#
#For example, here's a case-insensitive string comparison:
#
#>>> sorted("This is a test string from Andrew".split(), key=str.lower)
#['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']
#
#The value of the key parameter should be a function that takes a single argument and returns a key to use for sorting purposes. This technique is fast because the key function is called exactly once for each input record.
#
#A common pattern is to sort complex objects using some of the object's indices as a key. For example: 

##Learning to work with Key Sorts

def key_function(tuplex):
    length=int(len(tuplex)-1)
    tuplex=tuplex[length]
    return tuplex

print key_function((2,1,3,4))