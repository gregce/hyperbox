#Test FiLE

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
    

#Standard boilerplate to call main() function to begin 
#By doing the main check, you can have that code only execute when you want to run the module as a program and not have it execute when someone just wants to import your module and call your functions themselves.
if __name__ == '__main__':
    #main()
    print multiplystring('Test',1)
    
    #Fun fact, Python checks code at runtime, not compile time.
    
    #One file of Python code is called a *module*. The file "binky.py" is also known as the module "binky". 
    #A module essentially contains variable definitions like, "x = 6" and "def foo()". 
    #Suppose the file "binky.py" contains a "def foo()". The fully qualified name of that foo function is "binky.foo". 