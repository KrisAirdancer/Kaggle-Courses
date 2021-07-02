#########################
# Handling Missing Values
#########################

# Steps to cleaning a dataset

# STEP 1 - Set up your libraries and import the data files
"""
# modules we'll use
import pandas as pd
import numpy as np

# read in all our data
nfl_data = pd.read_csv("../input/nflplaybyplay2009to2016/NFL Play by Play 2009-2017 (v4).csv")

# set seed for reproducibility
np.random.seed(0) 
"""

# STEP 2 - Take a quick look at your imported data
# Get an idea of what your data looks like
"""
# look at the first five rows of the nfl_data file. 
# I can see a handful of missing data already!
nfl_data.head()
"""

# STEP 3 - Evaluate your missing data
"""
# get the number of missing data points per column
missing_values_count = nfl_data.isnull().sum()

# look at the # of missing points in the first ten columns
missing_values_count[0:10]

# how many total missing values do we have?
total_cells = np.product(nfl_data.shape)
total_missing = missing_values_count.sum()

# percent of data that is missing
percent_missing = (total_missing/total_cells) * 100
print(percent_missing)
"""

# STEP 4 - Figure out why the missing data is missing
"""
This is the point at which we get into the part of data science that I like to call
"data intution", by which I mean "really looking at your data and trying to figure out
why it is the way it is and how that will affect your analysis". It can be a frustrating
part of data science, especially if you're newer to the field and don't have a lot of
experience. For dealing with missing values, you'll need to use your intution to figure
out why the value is missing.

One of the most important questions you can ask yourself to help figure this out is this:

Is this value missing because it wasn't recorded or because it doesn't exist?

If a value is missing becuase it doesn't exist (like the height of the oldest child of
someone who doesn't have any children) then it doesn't make sense to try and guess what
it might be. These values you probably do want to keep as NaN. On the other hand, if a
value is missing because it wasn't recorded, then you can try to guess what it might have
been based on the other values in that column and row.

This is called imputation, and we'll learn how to do it next! :)


If data is missing because it simply doesn't exist (such as number of children for a couple
with no children), then it is best to replace all of the NaN values associated with this
data with a value that indicates "no children."
"""

# STEP 5 - Deal with the NaNs
"""
If you're in a hurry or don't have a reason to figure out why your values are missing,
one option you have is to just remove any rows or columns that contain missing values.
(Note: I don't generally recommend this approch for important projects! It's usually
worth it to take the time to go through your data and really look at all the columns
with missing values one-by-one to really get to know your dataset.)

If you're sure you want to drop rows with missing values, pandas does have a handy function,
dropna() to help you do this. Let's try it out on our NFL dataset!

# remove all the rows that contain a missing value:
nfl_data.dropna()

Alternatively we could drop the columns that contain a missing value:
# remove all columns with at least one missing value
columns_with_na_dropped = nfl_data.dropna(axis=1)
columns_with_na_dropped.head()
"""

# STEP 6 - Evaluate how much data you lost by removing the entire column and/or row
"""
# Just how much data did we lose?
print("Columns in original dataset: %d \n" % nfl_data.shape[1])
print("Columns with na's dropped: %d" % columns_with_na_dropped.shape[1])
"""

# STEP 7 - Fill in any missing values that you can
"""
We can use the Panda's fillna() function to fill in missing values in a dataframe for us.
One option we have is to specify what we want the NaN values to be replaced with. Here,
I'm saying that I would like to replace all the NaN values with 0.

# replace all NA's with 0
subset_nfl_data.fillna(0)

I could also be a bit more savvy and replace missing values with whatever value comes
directly after it in the same column. (This makes a lot of sense for datasets where the
observations have some sort of logical order to them.)

# replace all NA's the value that comes directly after it in the same column, 
# then replace all the remaining na's with 0
subset_nfl_data.fillna(method='bfill', axis=0).fillna(0)
"""

# Some helpful code examples
"""
# Problem 1
If you removed all of the rows of sf_permits with missing values, how many rows are left?
Note: Do not change the value of sf_permits when checking this.

sf_permits_less_NaN = sf_permits.dropna().sum()
print(sf_permits_less_NaN)

# Problem 2
Now try removing all the columns with empty values. Create a new DataFrame called
sf_permits_with_na_dropped that has all of the columns with empty values removed.
How many columns were removed from the original sf_permits DataFrame? Use this number to
set the value of the dropped_columns variable below.

sf_permits_with_na_dropped = sf_permits.dropna(axis=1)
​
cols_in_original_dataset = sf_permits.shape[1]
cols_in_na_dropped = sf_permits_with_na_dropped.shape[1]
dropped_columns = cols_in_original_dataset - cols_in_na_dropped

# Problem 3
Try replacing all the NaN's in the sf_permits data with the one that comes directly after
it and then replacing any remaining NaN's with 0. Set the result to a new DataFrame
sf_permits_with_na_imputed.

sf_permits_with_na_imputed = sf_permits.fillna(method='bfill', axis=0).fillna(0)
"""








