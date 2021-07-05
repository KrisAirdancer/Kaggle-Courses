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

###########################
# Scaling and Normalization
###########################

# Scaling
"""
- Scalilng changes the range of your data
- Normalization changes the shape and distribution of your data

Scaling
- This means that you're transforming your data so that it fits within a specific scale,
like 0-100 or 0-1. You want to scale data when you're using methods based on measures of
how far apart data points are
- Scaling allows us to compare different variables on the same scale, such as Yen vs Dollars.
- If you plot your data before and after scaling it, you will see that the plots have the
same shape, but that the x-axis has a different range - range changes, shape stays the same.

Example - If run, this will demonstrate scaling
# generate 1000 data points randomly drawn from an exponential distribution
original_data = np.random.exponential(size=1000)

# mix-max scale the data between 0 and 1
scaled_data = minmax_scaling(original_data, columns=[0])

# plot both together to compare
fig, ax = plt.subplots(1,2)
sns.distplot(original_data, ax=ax[0])
ax[0].set_title("Original Data")
sns.distplot(scaled_data, ax=ax[1])
ax[1].set_title("Scaled data")

"""

# Normalization
"""
- Normalization is the process of adjusting a dataset to have all of its data points evenly
distributed across a range of values.

- Normal distribution: Also known as the "bell curve", this is a specific statistical
distribution where a roughly equal observations fall above and below the mean, the mean
and the median are the same, and there are more observations closer to the mean. The normal
distribution is also known as the Gaussian distribution.

- In general, you'll normalize your data if you're going to be using a machine learning or
statistics technique that assumes your data is normally distributed. Some examples of these
include linear discriminant analysis (LDA) and Gaussian naive Bayes. (Pro tip: any method with
"Gaussian" in the name probably assumes normality.)

Example - If run, this will demonstrate normalization
# normalize the exponential data with boxcox
normalized_data = stats.boxcox(original_data)

# plot both together to compare
fig, ax=plt.subplots(1,2)
sns.distplot(original_data, ax=ax[0])
ax[0].set_title("Original Data")
sns.distplot(normalized_data[0], ax=ax[1])
ax[1].set_title("Normalized data")


"""

############################################
# Example Code for Scaling and Normalization
############################################

# Scaling Data
"""
## Setup

# modules we'll use
import pandas as pd
import numpy as np

# for Box-Cox Transformation
from scipy import stats

# for min_max scaling
from mlxtend.preprocessing import minmax_scaling

# plotting modules
import seaborn as sns
import matplotlib.pyplot as plt

# read in all our data
kickstarters_2017 = pd.read_csv("../input/kickstarter-projects/ks-projects-201801.csv")

# set seed for reproducibility
np.random.seed(0)

## Scaling Data

# select the usd_goal_real column
original_data = pd.DataFrame(kickstarters_2017.usd_goal_real)

# scale the goals from 0 to 1
scaled_data = minmax_scaling(original_data, columns=['usd_goal_real'])

# plot the original & scaled data together to compare
fig, ax=plt.subplots(1,2,figsize=(15,3))
sns.distplot(kickstarters_2017.usd_goal_real, ax=ax[0])
ax[0].set_title("Original Data")
sns.distplot(scaled_data, ax=ax[1])
ax[1].set_title("Scaled data")

## Compare our scaled data to our original data

print('Original data\nPreview:\n', original_data.head())
print('Minimum value:', float(original_data.min()),
      '\nMaximum value:', float(original_data.max()))
print('_'*30)

print('\nScaled data\nPreview:\n', scaled_data.head())
print('Minimum value:', float(scaled_data.min()),
      '\nMaximum value:', float(scaled_data.max()))
"""


# Normalizing Data
"""
## Setup

# get the index of all positive pledges (Box-Cox only takes positive values)
index_of_positive_pledges = kickstarters_2017.usd_pledged_real > 0

# get only positive pledges (using their indexes)
positive_pledges = kickstarters_2017.usd_pledged_real.loc[index_of_positive_pledges]

# normalize the pledges (w/ Box-Cox)
normalized_pledges = pd.Series(stats.boxcox(positive_pledges)[0], 
                               name='usd_pledged_real', index=positive_pledges.index)

# plot both together to compare
fig, ax=plt.subplots(1,2,figsize=(15,3))
sns.distplot(positive_pledges, ax=ax[0])
ax[0].set_title("Original Data")
sns.distplot(normalized_pledges, ax=ax[1])
ax[1].set_title("Normalized data")

## Compare original data to normalized data

print('Original data\nPreview:\n', positive_pledges.head())
print('Minimum value:', float(positive_pledges.min()),
      '\nMaximum value:', float(positive_pledges.max()))
print('_'*30)

print('\nNormalized data\nPreview:\n', normalized_pledges.head())
print('Minimum value:', float(normalized_pledges.min()),
      '\nMaximum value:', float(normalized_pledges.max()))

"""

###############
# Parsing Dates
###############

# Example Code
"""
## Read in data

# modules we'll use
import pandas as pd
import numpy as np
import seaborn as sns
import datetime

# read in our data
landslides = pd.read_csv("../input/landslide-events/catalog.csv")

# set seed for reproducibility
np.random.seed(0)

## Look at the specific part of the data we will be working with

# print the first few rows of the date column
print(landslides['date'].head())

## Checking the datatype of the data we are interested in

# check the data type of our date column
landslides['date'].dtype

Note: It is common to see dates entered as strings, which will be of the type 'Object'

- There are date-specific datatypes, so if you get the type "object" back, you know the
date isn't formatted as a date datatype.

Note: You may have to check the numpy documentation to match the letter code to the dtype
of the object. "O" is the code for "object", so we can see that these two methods give us
the same information.

## Parsing date strings as date types

Convert our date columns to datetime
Now that we know that our date column isn't being recognized as a date, it's time to convert
it so that it is recognized as a date. This is called "parsing dates" because we're taking in
a string and identifying its component parts.

We can pandas what the format of our dates are with a guide called as "strftime directive",
which you can find more information on at this link. The basic idea is that you need to point
out which parts of the date are where and what punctuation is between them. There are lots of
possible parts of a date, but the most common are %d for day, %m for month, %y for a two-digit
year and %Y for a four digit year.

Some examples:

1/17/07 has the format "%m/%d/%y"
17-1-2007 has the format "%d-%m-%Y"
Looking back up at the head of the "date" column in the landslides dataset, we can see that
it's in the format "month/day/two-digit year", so we can use the same syntax as the first
example to parse in our dates:

# create a new column, date_parsed, with the parsed dates
landslides['date_parsed'] = pd.to_datetime(landslides['date'], format="%m/%d/%y")

## Check that the parsing worked

# print the first few rows
landslides['date_parsed'].head()

NOTE:
If you run into an error while parsing dates that is caused by differently formatted dates
in the same column, you can have pandas try to infer what the right date format should be.
You can do that like so using infer_datetime_format=true:
landslides['date_parsed'] = pd.to_datetime(landslides['Date'], infer_datetime_format=True)

It is NOT best practice to always use the built in date format inferrer,
There are two big reasons not to always have pandas guess the time format. The first is that
pandas won't always been able to figure out the correct date format, especially if someone has
gotten creative with data entry. The second is that it's much slower than specifying the exact
format of the dates.

## Extracting some of the date we want

# get the day of the month from the date_parsed column
day_of_month_landslides = landslides['date_parsed'].dt.day
day_of_month_landslides.head()

## Double checking our date data
- It is possible that we got our months and days mixed up durign parsing. As such, it is best
to simply check that all of the day or month values fall within the expected range of 
31 days or 12 months repectively by charting them on a histogram (below checks the days).

# remove na's
day_of_month_landslides = day_of_month_landslides.dropna()

# plot the day of the month
sns.distplot(day_of_month_landslides, kde=False, bins=31)
"""

#####################
# Character Encodings
#####################

"""
- Character encoding are the rules that dictate how to map binary (011001011001) to human
readable data ("hi").
- When the wrong encoding (rule set) is used, the output is called 'mojibake' (moh-jee-ba-kay),
which is a fun name for jiberish - it is also possible to get unknown characters (question mark
in a diamond), which are the characters that are displayed when the passed binary doesn't
map to any specific character.

- UTF-8 is the most common character encoding in Python, so one should generally use UTF-8 encoding
for their data.

- You can change the encoding of an object in Python using the encode() function:
# start with a string
before = "This is the euro symbol: €"

# check to see what datatype it is
type(before)
str

# encode it to a different encoding, replacing characters that raise errors
after = before.encode("utf-8", errors="replace")

# check the type
type(after)

NOTE: !!! - Importantly, if you use the wrong encoding for a set of data then try to 
decode it back to the correct encoding, it is possible, and not uncommon, for data to
be lost - that is some of the characters will be unrecognizable when they are decoded
back, making the data unusable!
"""

#########################################
# Reading in files with encoding problems
#########################################
"""
- Sometimes when reading data into Python, we will get an error due to the dataset being
encoded in something other than UTF-8 - Python defaults to UTF-8 - There are two ways to
go about handling this:
    - 1) Guess at a few encodings to see if one works - this is slow and tedius
    - 2) Use the chardet.detect() function to "detect" the correct encoding -  faster, but doesn't work 100% of the time though

- chardet.detect() function example:
# look at the first ten thousand bytes to guess the character encoding
with open("../input/kickstarter-projects/ks-projects-201801.csv", 'rb') as rawdata: result = chardet.detect(rawdata.read(10000))

- Once you work out the correct encoding, it is best to save the dataset as UTF-8 afterward
so you don't have to go through the guessing and re-encoding process again. This is easy to
do as Python will automatically save your data as UTF-8:

# save our file (will be saved as UTF-8 by default!)
kickstarter_2016.to_csv("ks-projects-201801-utf8.csv")




"""




