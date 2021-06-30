###########################
#Kaggle Pandas Course Notes
###########################

"""
To import pandas, we simply write
import pandas

Alternatively, we can import it with a name that is easier to work with.
import pandas as pd
"""
import pandas as pd

# Pandas creates two core objects: DataFrame and Series

############
# DataFrames
############

# DataFrames are tables that contain data
testFrame = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
print(testFrame)
# The same thing can also be written, fruits = pd.DataFrame([[30, 21]], columns=['Apples', 'Bananas'])

# Any type of data (integers, strings, etc.)

"""
We are using the pd.DataFrame() constructor to generate these DataFrame objects.
The syntax for declaring a new one is a dictionary whose keys are the column names
(Bob and Sue in this example), and whose values are a list of entries. This is the
standard way of constructing a new DataFrame, and the one you are most likely to encounter.

The dictionary-list constructor assigns values to the column labels, but just uses an
ascending count from 0 (0, 1, 2, 3, ...) for the row labels. Sometimes this is OK, but
oftentimes we will want to assign these labels ourselves.

The list of row labels used in a DataFrame is known as an Index. We can assign values
to it by using an index parameter in our constructor:
"""
# Adding row names to a DataFrame
testFrame = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
			  'Sue': ['Pretty good.', 'Bland.']},
			 index=['Product A', 'Product B'])
print(testFrame)

# Two ways to create a DataFrame:
fruit_sales = pd.DataFrame([[35, 21], [41, 34]], columns=['Apples', 'Bananas'],
                index=['2017 Sales', '2018 Sales'])
print(fruit_sales)

fruit_sales = pd.DataFrame({'Apples': [35, 41], 'Bananas': [21, 34]},
				index=['2017 Sales', '2018 Sales'])
print(fruit_sales)

########
# Series
########






