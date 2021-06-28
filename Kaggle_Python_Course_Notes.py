


# MODULE 2 - Functions and Getting Help

help(round) # Provides info about the method whose name you pass as a parameter

# Declaring a method in Python
def myMethodName(parameters): # Don't forget the colon
    """ Triple quotes demarkate a Docstring. These are docuemntation
    comments used by Python - much like JavaDocs in Java.
    If they come right after a method header, the help()
    method will return the comment text when it is called
    with that method's name.

    Example method calls can be included in Docstrings using >>>
    That is >>> least_difference(1, 5, 10)
    These examples will show up when help() is called.

    Docstrings can also be demarkated using a double coat (two quote marks)
   instead of a triple coat.

    Double and triple coats can also be used as multi-line comments
    if they are included in a location other than immedieately following
    a function header.
    """
    return 1 + 2 # Return works the same in PY as in Java

"""
Functions that don't have a return value and don't make any lasting
changes when they run (such as modifying an array, etc.), they are
given a default return value of None.
"""

# The print() function allows us to pass a character to be used as a 
# separator between the elements to be printed. This defaults to 
# a single space.
print(1, 2, 3, sep=' < ')

# Functions can be passed as parameters of other functions. The below prints 5\n25
def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1), 
    sep='\n', # '\n' is the newline character - it starts a new line
)

"""
Another example. This one returns

Which number is biggest?
100
Which number is the biggest modulo 5?
14
"""
def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)



# MODULE 3 - 
