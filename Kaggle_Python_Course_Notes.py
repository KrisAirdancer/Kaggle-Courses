

#######################################
# MODULE 2 - Functions and Getting Help
#######################################

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


# The Pass keyword literlly does nothing. We can use it to prevent Python from
# giving us an error when building out a method b/c Python will give an error
# if the method body is left blank. We simply add Pass to the method body and the 
# issue goes away.


# The round method can be called with negative values for the number of places to round to.
# In doing so, it will round to the nearest 1s, 10s, 100s, etc. place
print(round(12345, -2)) # Returns 12300

"""
In a method header, the notation parameter_name=default_value can be used to set a default
value to be passed if that parameter isn't passed a value by the method call.
"""
def to_smash(total_candies,num_friends=3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    return total_candies % num_friends

print(to_smash(91)) # Returns 1, b/c doefaults to 3
print(to_smash(99, 11)) # Returns zero


######################################
# MODULE 3 - Booleans and Conditionals
######################################

# Boolean values in Py are represented as bool and hold the value of true or false

# Boolean operators (==, !=, <, etc.) are the same as in Java

# To combine boolean operators in Py, we use and, not, and or

print(3 == 4 and 3==3) # Returns false
print(3 == 4 or 3 == 3) # Returns true


# When working with a large chunk of boolean expressions, use parenteses and break the 
# code up over several lines to help emphasize the strucutre of the statement.
have_umbrella =  True
rain_level = 3
have_hood = False
is_workday = True
prepared_for_weather = (
    have_umbrella 
    or ((rain_level < 5) and have_hood) 
    or (not (rain_level > 0 and is_workday))
)

##############
# CONDITIONALS
##############

# Py uses the conditional statements if, else, and elif (else if)
# Note that else if does NOT work, it must be formatted as elif.

"""
The : is used to indicate the start of a code block.

Note especially the use of colons (:) and whitespace to denote separate blocks of code.
This is similar to what happens when we define a function - the function header ends with :,
and the following line is indented with 4 spaces. All subsequent indented lines belong to
the body of the function, until we encounter an unindented line, ending the function definition.
"""

# Example use of the :
def f(x):
    if x > 0:
        print("Only printed when x is positive; x =", x)
        print("Also only printed when x is positive; x =", x)
    print("Always printed, regardless of x's value; x =", x)

f(1)
f(0)


"""
Like the int() and float() functions that turn the passed values into integers and floats respectively,
the bool() function turns things into boolean values, true and false.
"""
print(bool(1)) # all numbers are treated as true, except 0
print(bool(0))
print(bool("asf")) # all strings are treated as true, except the empty string ""
print(bool(""))
# Generally empty sequences (strings, lists, and other types we've yet to see like lists and tuples)
# are "falsey" and the rest are "truthy"

"""
!!! - NOTE: We can use non-boolean objects in if conditions and other places where a boolean
would be expected. Python will implicitly treat them as their corresponding boolean value:
"""

# A note on using the print() function. You can include the conditional statement in the print() call.
total_candies = 45
if total_candies == 1:
    print("Splitting 1 candy")
else:
    print("Splitting", total_candies, "candies")
#Here's a slightly more succinct solution using a conditional expression:
print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")

"""
The not keyword inverts the value of a Boolean expression. For instance, the not keyword
flips the value of True to False.
"""

# An example of an "exclusive or" (the default or in Py is inclusive)
ketchup = True
mustard = True
onion = True
def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    return (ketchup and not mustard) or (mustard and not ketchup)

"""
An interesting appliction of the int() function.

We’ve seen that calling bool() on an integer returns False if it’s equal to 0 and True otherwise.
What happens if we call int() on a bool? Try it out in the notebook cell below.

Can you take advantage of this to write a succinct function that corresponds to the English sentence
"does the customer want exactly one topping?"?
"""

def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    sum = int(ketchup) + int(mustard) + int(onion)
    
    return sum == 1

"""
This condition would be pretty complicated to express using just and, or and not,
but using boolean-to-integer conversion gives us this short solution:
"""

# return (int(ketchup) + int(mustard) + int(onion)) == 1

"""
Fun fact: we don't technically need to call int on the arguments. Just by doing addition with booleans,
Python implicitly does the integer conversion. So we could also write...
"""

# return (ketchup + mustard + onion) == 1


##################
# MODULE 4 - Lists
##################

# Example list
primes = [2, 3, 11, 5, 7]

# You can make a list of nearly anything, ints, floats, strings, even other lits.
hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # (Comma after the last element is optional)
]
# (I could also have written this on one line, but it can get hard to read)
hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]

# One can even mix variable types in a single list
my_favourite_things = [32, 'raindrops on roses', help]
# (Yes, Python's help function is *definitely* one of my favourite things)

# Py uses indexing for lists, just like Java. The index starts at zero, just like Java.
my_favourite_things[0] # Yields 32

# !!! - Note: Elements at the end of the list can be accessed with negative numbers, starting from -1:
my_favourite_things[-1] # Yields the help function

# A set of items can be returned from a list using slicing:
primes[0:2] # Returns 2, 3
# Note: Slicing goes up to, but does not include, the index value after the :
# The starting and ending values are optional and the beginning and ends of the list will be used as default
primes[:2] # Is the same as above

# Negative indicies can also be used in slicing
primes[0:-2] # Returns 2, 3, 5 Note that the element at the negative index is included in the return

# Lists are mutable and can be changed in-place
primes[0] = 17

#####################
# FUNCTIONS FOR LISTS
#####################

# The len() function can be used to get the length of a list
len(primes)

# The sorted() function returns a sorted version of the list
# !!! - Note: The sorted() function does NOT modify the original list
print("Sorted List: ", sorted(primes))
print("Original List: ", primes)
new_list = sorted(primes)
# However, the sorted list can be assigned to a variable and retain the sorting - that is, sorted() is making a new list instance
print("new_list: ", new_list)

# The sum() function sums the values in the list
sum(primes)

# The min() and max() functions can accept a single list as a parameter
min(primes)
max(primes)

###################
# Objects in Python
###################

# Everyting in Py in an object.
# Objects have both attributes (variablesa) and functions (methods)
# The attributes and functions of an object can be accessed using dot syntax

# For example, numbers have a method called bit_length. Again, we access it using dot syntax:
x = 10
x.bit_length
# Output: <function int.bit_length()>
# To actually call it, we add parentheses:
x.bit_length()

# Object methods can also be passed to the help() function
help(x.bit_length)

###################
# Methods for lists
###################

# list.append modifies a list by adding an item to the end
primes.append(13)

# Side note: The -> None part of a help() output tells us that the method doesn't return anything.
# This is part of the output you will get if you call help() on a list object.

# list.pop removes and returns the last element of a list
primes.pop() # Defaults to the last element in the list

#################
# Searching Lists
#################

# list.index() returns the index value of a specified object in a list.
# Note: If the element does not exist in the list, an error will be thrown.

# The in keyword can be used to determine if a particluar object exists in a list
13 in primes # Returns True

# The help() function can be used to get a list of the methods that a particular object has

########
# Tuples
########

"""
Tuples are basically lists except that,
1. The syntax used to create them uses parentheses instead of square brackets
2. They are immutable
"""

# Creating a tuple
prime_tuple = (2, 3, 7, 13)

# That Python trick a, b = b, a
# The formula a, b = b, a can be used to swap variables a and b without using a third temp variable
# That said, I don't know how this works. The course says it takes advantage of tuples.


#########################################
# MODULE 5: Loops and List Comprehensions
#########################################

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

def planet_loop(planets):
    for planet in planets:
        print(planet, end=' ') # print all on same line

"""
The for loop specifies the variable name to use (in this case, planet)
the set of values to loop over (in this case, planets)

You use the word "in" to link them together.
The object to the right of the "in" can be any object that supports iteration.
Basically, if it can be thought of as a group of things, you can probably loop over it.
In addition to lists, we can iterate over the elements of a tuple:
"""

multiplicands = (2, 2, 2, 3, 3, 5)

def mulitply(multiplicands):
    product = 1
    for mult in multiplicands:
        product = product * mult
    product

# One can loop over any type of list

# The range() function can be used with for loops to repeat certain tasks
for i in range(5):
    print("Example number ", i)

# while loops iterate until a condition is met
index = 0
while index < 10:
    print(index, end=' ')
    index += 1


#####################
# List Comprehensions
#####################

"""
List comprehensions is a way to generate a list of related
elements. Such as all of the values from 1 to 100 squared.
(see example below)
The general format for a list comprehension is:

NOTE: Expression means an expression for each term in the list

[expression for value in collection] A basic LC

[expresion for value in collection if <test>] An LC using conditionals.
Elements will only be included in the list if they satisfy the conditional statement.

[expression for value in collection if <test1> and <test2>] An LC where both
conditionals must be true for an item to be included in the list

See here for help with this: https://www.youtube.com/watch?v=AhSvKGTh28Q&ab_channel=Socratica
"""

# NOTE: Exponents in Python are represented with double asteriks **

# Example of populating a list WITHOUT list comprehensions
squares = [] # An empty list to start
for i in range(1, 100): # Loop over the range of values, square them, and add them to the squares list
    squares.append(i**2) # Square each value and add it to the list

print(squares)

# Example of populating a list WITH list comprehensions
squares2 = [i**2 for i in range(1, 100)]
print(squares2)

# List Comprehensions can be used for things other than generating lists
# Example of using LC to count the numbner of negative values (-1, -2, -3, etc.) in a list
def count_negatives(nums):
    return len([num for num in nums if num < 0])

# List comprehensions allow for some great one liners, but overusing one liners can lead to worse coding solutions
# in terms of readability and understandability.
# See the Zen of Python for more on this: https://en.wikipedia.org/wiki/Zen_of_Python
# When in doubt, choose the code that will be easiest for others to understand.

####################################################
# Part 2 of Module 5 - Loops and List Comprehensions
####################################################

# The following returns items in the list for num in nums that meet the expression num & 7 == 0 
def has_lucky_number(nums):
    return any([num % 7 == 0 for num in nums])

# The Monte Carlo Method
"""
This is a method of determining the average result of some activity or occurance.
We simulate the event many, many times, then average the outcome of all of the
simulations to get the average outcome for any given occurance.

This can be used to estimate slot machine earnings, stock market performance, etc.
"""

#####################################
# MODULE 6 - Strings and Dictionaries
#####################################

"""
Strings can be defined using either "double" or 'single' quotations.
Double quotes are usefull if your string contains single quote characters
or vice-versa.
"""
print("Pluto's a planet!")
print('My dog is named "Pluto"')
# We can also "escape" internal quotes using a backslash
print('Pluto\'s a planet!')

# Some other uses of the backslash are as follows:
print('A single quote \'')
print("A double quote \"")
print("A backslash \\")
print("A return \n See, a new line!")

# Another way to create a new line is with triple quotes """
print("""hello
world""")

# The default end= value for print() is a newline character
print("hello")
print("world")
print("hello", end='')
print("pluto", end='')
print("\n")

# Strings are effectively lists and we can do operations on them largely as if they are a list
# HOWEVER, strings in Py are immutable - they cannot be modified

planet = "Neptune"
# Indexing
print(planet[0])
# Slicing
print(planet[-3:])
# Length
print(len(planet))
# Looping
print([char+'! ' for char in planet])

# See, no chaning them
# planet[0] = 'B' This would throw an error if run!

##################################
# Methods for working with strings
##################################

# Uppercase
planet.upper()
# Lowercase
planet.lower()
# Find the first index of a substring
planet.index('ept')

# Splitting a string into a list of substrings (defaults to split on whitespace)
lovemuffin = "Leauge Of Villanous Evildoers Maniacally United For Firghtening Investments In Naughtiness"
print(lovemuffin.split())
# You can pass a value to split on instead of whitespace
print(lovemuffin.split('e'))

# A set of strings can be joined by calling the join() function on the operator you want placed between the strings
some_strings = ["Here", "are", "some", "strings"]
print(some_strings)
print('-'.join(["Here", "are", "some", "strings"]))
print('+'.join(some_strings))

# We can also include unicode 👏 in our string literals
print("See, unicode 👏!") # Although, this won't print the hands to the console...

# We can concatonate strings using the + operator
print("Con" + "cat" + "o" + "nate")
# IF we want to concatonate non-string objects, we simply call str() on them
print("Con" + "cat" + str(0) + "nate")
# We can use the format() function to make concatenating code clearer
print("Check {} out".format("this"))

# Another example of function()
pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
# 2 decimal points, 3 decimal points, format as percent, separate with commas
print("{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
planet, pluto_mass, pluto_mass / earth_mass, population,
))


# Dictionaries in Py are roughly the same as Hashmaps in Java - they map key-value pairs
numbers = {'one':1, 'two':2, 'three':3} # Here, 'one', 'two', and 'three' are keys and 1, 2, 3 are values
# The values can be accessed using the keys
print(numbers['one'])
# New values can be added as follows
numbers['four'] = 4
print(numbers)
# Values can be changed the same way
numbers['one'] = 'Hello!'
print(numbers)

# Py allows us to use dictionary comprehensions - similar to list comprehensions - to make dictionaries
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)

# The in operator can be used to tell us if something is in a dictionary
print('Saturn' in planet_to_initial)

# We can also loop over the keys in a dictionary with a for loop
for k in numbers:
    print("{} = {}".format(k, numbers[k]))

# We can access all of the keys and values in a dictionary using the keys() and values() functions
print(planet_to_initial.keys())
print(planet_to_initial.values())

# We can acces the key-value pairs simultaneously using items() NOTE: In Py, items refers to key-value pairs, one pair is one item
print(planet_to_initial.items())
# Or we can format the output
for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))

help(str)

#################################
# Working with External Libraries
#################################

# New libraries and modules can be imported using the import keyword
import math # Importing the math module from the standard Py library

# The math module contains a bunch of pre-defined variables for our use
print(math.pi)

# math.log() returns the natural logarithm of the expression - defaults to base 3, but can be set to any other base

# You can call help on libraries and modules
help(math)

# If we know we'll be using functions in math frequently we can import it under a shorter alias to save some typing (though in this case "math" is already pretty short).
import math as mt
print(mt.pi)
"""
Note: it is common convention to do this with popular libraries, such as
to import numpy as np and import pandas as pd.
"""

# We can also access all of the variables without the dot notation using import *
# import * makes all the module's variables directly accessible to you (without any dotted prefix).
from math import *
print(pi, log(32, 2))
"""
!!! - Note: Many libraries share variable names. If you import from multiple libraries
you should make sure to avoid using import *, as it can cause errors when the compiler
doesn't know what library to pull a variable from.

It is best practice to simply avoid using import *.
"""

# Another option for imports is to import only the variables you need from a particular library
from math import log, pi

# Note that some libraries actually utilize other libraries. These are called sub-modules
# The random library within the Numpy library is an example of this.
import numpy
print("numpy.random is a", type(numpy.random))
print("it contains names such as...",
      dir(numpy.random)[-15:]
     )

# Tips for working with strange/unknown stuff from imported libraries

# Tip 1: Utilize type() - This function tells us what type of object something is.
print(type(planet_to_initial))

# Tip 2: Utilize dir() - This returns a list of attributes (variables) from an object
dir()

# mean() returns the average value from an object
# toList() turns an array into a list

# Tip 3: Utilize help()

# Tip 4: Check the online docs for the function/library you are working with

######################
# Operator Overloading
######################

# Note: Arrays exist only in numpy, in vanilla Py they are called lists and they BEHAVE DIFFERENTLY!
"""
If one adds a value to a list, you get an error [10, 3, 5, 7, 8] + 10 -> ERROR
If you do the same to a numpy array, you add the value to all of the elements
in the array. [10, 3, 5, 7, 8] + 10 -> [20, 13, 15, 17, 18]
"""

"""
Simply put, operator overloading is when an operator performs differently in
different circumstances.
"""

# Here is a helpful way to change the format of tick-marks on graphs.
"""
ticks = graph.get_yticks()
# Format those values into strings beginning with dollar sign
new_labels = ['${}'.format(int(amt)) for amt in ticks]
# Set the new labels
graph.set_yticklabels(new_labels)
"""

# A helpful bit of example code
"""
def hand_total(hand):
    # Helper function to calculate the total points of a blackjack hand.
 
    total = 0
    # Count the number of aces and deal with how to apply them at the end.
    aces = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            total += 10
        elif card == 'A':
            aces += 1
        else:
            # Convert number cards (e.g. '7') to ints
            total += int(card)
    # At this point, total is the sum of this hand's cards *not counting aces*.

    # Add aces, counting them as 1 for now. This is the smallest total we can make from this hand
    total += aces
    # "Upgrade" aces from 1 to 11 as long as it helps us get closer to 21
    # without busting
    while total + 10 <= 21 and aces > 0:
        # Upgrade an ace from 1 to 11
        total += 10
        aces -= 1
    return total

def blackjack_hand_greater_than(hand_1, hand_2):
    total_1 = hand_total(hand_1)
    total_2 = hand_total(hand_2)
    return total_1 <= 21 and (total_1 > total_2 or total_2 > 21)
"""







