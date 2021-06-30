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


#################################
# Indexing, Selecting & Assigning
#################################

# Properties and indexing in Py objects
"""
In Python, we can access the property of an object by accessing it as an attribute.
A book object, for example, might have a title property, which we can access by calling
book.title. Columns in a pandas DataFrame work in much the same way.

# reviews.country # This returns a Series object

If we have a Python dictionary, we can access its values using the indexing ([]) operator.
We can do the same with columns in a DataFrame:

# reviews['country'] # Note that this returns a Series object (remember, a DataFrame is just a bunch of Series "glued" together

Note: reviews.country and reviews['country'] are effectively the same, but the second
is able to handle reserved character, such as spaces.

We can use the indexing operator twice to pull, first, a column (Series), then, second,
an item from that column: reviews['country'][0]

Here are a few other ways to do this:
reviews.description.iloc[0]
reviews.description.loc[0]
reviews.description[0]
"""

# More on indexing in Pandas

# Index-based selection selects data based on it's numerical position in the data set.
"""
To select the first row of data in a DataFrame, we may use the following:
reviews.iloc[0]

Both loc and iloc are row-first, column-second. This is the opposite of what we do in
native Python, which is column-first, row-second.

To get a column with iloc, we can do the following:
reviews.iloc[:, 0]

It's also possible to pass a list:
reviews.iloc[[0, 1, 2], 0]

Finally, it's worth knowing that negative numbers can be used in selection. This will
start counting forwards from the end of the values. So for example here are the last
five elements of the dataset.

reviews.iloc[-5:]
"""

# Label-based selection
"""
In label-based selection it is the data index value, not its position, which matters.
For example, to get the first entry in reviews, we would now do the following:

reviews.loc[0, 'country']

iloc is conceptually simpler than loc because it ignores the dataset's indices.
When we use iloc we treat the dataset like a big matrix (a list of lists), one
that we have to index into by position. loc, by contrast, uses the information
in the indices to do its work. Since your dataset usually has meaningful indices,
it's usually easier to do things using loc instead. For example, here's one operation
that's much easier using loc:

reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]

Another example:

reviews.loc[[0,1,10,100],['country', 'province', 'region_1', 'region_2']]
"""

# Choosing between loc and iloc
"""
When choosing or transitioning between loc and iloc, there is one "gotcha" worth keeping in mind, which is that the two methods use slightly different indexing schemes.

iloc uses the Python stdlib indexing scheme, where the first element of the range is included and the last one excluded. So 0:10 will select entries 0,...,9. loc, meanwhile, indexes inclusively. So 0:10 will select entries 0,...,10.

Why the change? Remember that loc can index any stdlib type: strings, for example. If we have a DataFrame with index values Apples, ..., Potatoes, ..., and we want to select "all the alphabetical fruit choices between Apples and Potatoes", then it's a lot more convenient to index df.loc['Apples':'Potatoes'] than it is to index something like df.loc['Apples', 'Potatoet'] (t coming after s in the alphabet).

This is particularly confusing when the DataFrame index is a simple numerical list, e.g. 0,...,1000. In this case df.iloc[0:1000] will return 1000 entries, while df.loc[0:1000] return 1001 of them! To get 1000 elements using loc, you will need to go one lower and ask for df.loc[0:999].

Otherwise, the semantics of using loc are the same as those for iloc.
"""

# Manipulating Indicies
"""
Note that the index we use is not immutable. We can manipulate the index in any way we see fit.
The set_index() method can be used to do the job. Here is what happens when we set_index to the
title field:

reviews.set_index("title")

Essentially, you can change index names as needed.
"""

# Conditional Selection of Data
"""
We an select columns/rows of data that meet certain criteria:

reviews.country == 'Italy'

The above produces a Series containing True/False boolean values based on the country of
each record. This result can then be used inside of loc to select the relevant data:

reviews.loc[reviews.country == 'Italy']
Can also be written: reviews[reviews.country == 'Italy'] although this is discouraged

We can use the ampersand (&) to use two conditions in the same statement:
reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]

We can use the pipe (|) operator as an or operator to do the same thing:
reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]

Pandas comes with a few built-in conditional selectors, two of which we will highlight here.

The first is isin. isin is lets you select data whose value "is in" a list of values.
For example, here's how we can use it to select wines only from Italy or France:

reviews.loc[reviews.country.isin(['Italy', 'France'])]

The second is isnull (and its companion notnull). These methods let you highlight values
which are (or are not) empty (NaN). For example, to filter out wines lacking a price tag
in the dataset, here's what we would do:

reviews.loc[reviews.price.notnull()]
"""

# Assigning data
"""
Going the other way, assigning data to a DataFrame is easy. You can assign either a
constant value:

reviews['critic'] = 'everyone'
reviews['critic']

Or with an iterable of values:

reviews['index_backwards'] = range(len(reviews), 0, -1)
reviews['index_backwards']
"""




