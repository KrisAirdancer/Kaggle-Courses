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

# A Series is a sequence of data values. If a DataFrame is a table, a Series is a list.
# And in fact you can create one with nothing more than a list:
print(pd.Series([1, 2, 3, 4, 5]))

# A Series is, in essence, a single column of a DataFrame. So you can assign column
# values to the Series the same way as before, using an index parameter. However, a
# Series does not have a column name, it only has one overall name:

print(pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A'))

# A DataFrame is essentially just a bunch of Series "glued" together.

####################
# Reading Data Files
####################

# CSV files are the most common type of data file.

# pd.read_csv() can be used to read a CSV file into a DataFrame
# newFrame = pd.read_csv(FILE DIRECTORY)

# The .shape() function can be used to check the size of the DataFrame.
# The output is (TOTAL NUMBER OF DATAPOINTS, NUMBER OF COLUMNS)	

# The .head() function pulls the first 5 rows of data.
# NOTE: The first row is numbered 0 - that is, the row index starts at 0 like everything else.

"""
The pd.read_csv() function is well-endowed, with over 30 optional parameters you can specify. 
For example, you can see in this dataset that the CSV file has a built-in index, which pandas
did not pick up on automatically. To make pandas use that column for the index (instead of
creating a new one from scratch), we can specify an index_col.
"""
# wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
# print(wine_reviews.head())

# To write to a csv we can use, DataFrame.to_csv()





