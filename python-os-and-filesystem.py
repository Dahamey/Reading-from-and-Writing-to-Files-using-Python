#!/usr/bin/env python
# coding: utf-8

# # Reading from and Writing to Files using Python
# 
# ![](https://i.imgur.com/rv8wZ7l.png)
# 
# 
# 
# 
# This tutorial series is a beginner-friendly introduction to programming and data analysis using the Python programming language. These tutorials take a practical and coding-focused approach. The best way to learn the material is to execute the code and experiment with it yourself. Check out the full series here: 
# 
# 1. [First Steps with Python and Jupyter](https://jovian.ai/aakashns/first-steps-with-python)
# 2. [A Quick Tour of Variables and Data Types](https://jovian.ai/aakashns/python-variables-and-data-types)
# 3. [Branching using Conditional Statements and Loops](https://jovian.ai/aakashns/python-branching-and-loops)
# 4. [Writing Reusable Code Using Functions](https://jovian.ai/aakashns/python-functions-and-scope)
# 5. [Reading from and Writing to Files](https://jovian.ai/aakashns/python-os-and-filesystem)
# 6. [Numerical Computing with Python and Numpy](https://jovian.ai/aakashns/python-numerical-computing-with-numpy)
# 7. [Analyzing Tabular Data using Pandas](https://jovian.ai/aakashns/python-pandas-data-analysis)
# 8. [Data Visualization using Matplotlib & Seaborn](https://jovian.ai/aakashns/python-matplotlib-data-visualization)
# 9. [Exploratory Data Analysis - A Case Study](https://jovian.ai/aakashns/python-eda-stackoverflow-survey)
# 

# This tutorial covers the following topics:
# 
# - Interacting with the filesystem using the `os` module
# - Downloading files from the internet using the `urllib` module
# - Reading and processing data from text files
# - Parsing data from CSV files into dictionaries & lists
# - Writing formatted data back to text files

# ### How to run the code
# 
# This tutorial is an executable [Jupyter notebook](https://jupyter.org) hosted on [Jovian](https://www.jovian.ai). You can _run_ this tutorial and experiment with the code examples in a couple of ways: *using free online resources* (recommended) or *on your computer*.
# 
# #### Option 1: Running using free online resources (1-click, recommended)
# 
# The easiest way to start executing the code is to click the **Run** button at the top of this page and select **Run on Binder**. You can also select "Run on Colab" or "Run on Kaggle", but you'll need to create an account on [Google Colab](https://colab.research.google.com) or [Kaggle](https://kaggle.com) to use these platforms.
# 
# 
# #### Option 2: Running on your computer locally
# 
# To run the code on your computer locally, you'll need to set up [Python](https://www.python.org), download the notebook and install the required libraries. We recommend using the [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/) distribution of Python. Click the **Run** button at the top of this page, select the **Run Locally** option, and follow the instructions.
# 
# >  **Jupyter Notebooks**: This tutorial is a [Jupyter notebook](https://jupyter.org) - a document made of _cells_. Each cell can contain code written in Python or explanations in plain English. You can execute code cells and view the results, e.g., numbers, messages, graphs, tables, files, etc., instantly within the notebook. Jupyter is a powerful platform for experimentation and analysis. Don't be afraid to mess around with the code & break things - you'll learn a lot by encountering and fixing errors. You can use the "Kernel > Restart & Clear Output" menu option to clear all outputs and start again from the top.

# ## Interacting with the OS and filesystem
# 
# The `os` module in Python provides many functions for interacting with the OS and the filesystem. Let's import it and try out some examples.

# In[1]:


import os


# We can check the present working directory using the `os.getcwd` function.

# In[2]:


os.getcwd()


# To get the list of files in a directory, use `os.listdir`. You pass an absolute or relative path of a directory as the argument to the function.

# In[3]:


help(os.listdir)


# In[4]:


os.listdir('.') # relative path


# In[5]:


os.listdir('/usr') # absolute path


# You can create a new directory using `os.makedirs`. Let's create a new directory called `data`, where we'll later download some files.

# In[6]:


os.makedirs('./data', exist_ok=True)


# Can you figure out what the argument `exist_ok` does? Try using the `help` function or [read the documentation](https://docs.python.org/3/library/os.html#os.makedirs).
# 
# Let's verify that the directory was created and is currently empty.

# In[7]:


'data' in os.listdir('.')


# In[8]:


os.listdir('./data')


# Let us download some files into the `data` directory using the `urllib` module.

# In[9]:


url1 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans1.txt'
url2 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans2.txt'
url3 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans3.txt'


# In[10]:


from urllib.request import urlretrieve


# In[11]:


urlretrieve(url1, './data/loans1.txt')


# In[12]:


urlretrieve(url2, './data/loans2.txt')


# In[13]:


urlretrieve(url3, './data/loans3.txt')


# Let's verify that the files were downloaded.

# In[14]:


os.listdir('./data')


# You can also use the [`requests`](https://docs.python-requests.org/en/master/) library to dowload URLs, although you'll need to [write some additional code](https://stackoverflow.com/questions/44699682/how-to-save-a-file-downloaded-from-requests-to-another-directory) to save the contents of the page to a file.

# ## Reading from a file 
# 
# To read the contents of a file, we first need to open the file using the built-in `open` function. The `open` function returns a file object and provides several methods for interacting with the file's contents.

# In[15]:


file1 = open('./data/loans1.txt', mode='r')


# The `open` function also accepts a `mode` argument to specifies how we can interact with the file. The following options are supported:
# 
# ```
#     ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     'U'       universal newline mode (deprecated)
#     ========= ===============================================================
# ```
# 
# To view the contents of the file, we can use the `read` method of the file object.

# In[16]:


file1_contents = file1.read()


# In[17]:


print(file1_contents)


# The file contains information about loans. It is a set of comma-separated values (CSV). 
# 
# > **CSVs**: A comma-separated values (CSV) file is a delimited text file that uses a comma to separate values. Each line of the file is a data record. Each record consists of one or more fields, separated by commas. A CSV file typically stores tabular data (numbers and text) in plain text, in which case each line will have the same number of fields. (Wikipedia)
# 
# The first line of the file is the header, indicating what each of the numbers on the remaining lines represents. Each of the remaining lines provides information about a loan. Thus, the second line `100000,36,0.08,20000` represents a loan with:
# 
# * an *amount* of `$100000`, 
# * *duration* of `36` months, 
# * *rate of interest* of `8%` per annum, and 
# * a down payment of `$20000`
# 
# The CSV is a standard file format used for sharing data for analysis and visualization. Over the course of this tutorial, we will read the data from these CSV files, process it, and write the results back to files. Before we continue, let's close the file using the `close` method (otherwise, Python will continue to hold the entire file in the RAM)

# In[18]:


file1.close()


# Once a file is closed, you can no longer read from it.

# In[19]:


file1.read()


# ## Closing files automatically using `with`
# 
# To close a file automatically after you've processed it, you can open it using the `with` statement.

# In[20]:


with open('./data/loans2.txt') as file2:
    file2_contents = file2.read()
    print(file2_contents)


# Once the statements within the `with` block are executed, the `.close` method on `file2` is automatically invoked. Let's verify this by trying to read from the file object again.

# In[21]:


file2.read()


# ## Reading a file line by line
# 
# 
# File objects provide a `readlines` method to read a file line-by-line. 

# In[22]:


with open('./data/loans3.txt', 'r') as file3:
    file3_lines = file3.readlines()


# In[23]:


file3_lines


# ## Processing data from files
# 
# Before performing any operations on the data stored in a file, we need to convert the file's contents from one large string into Python data types. For the file `loans1.txt` containing information about loans in a CSV format, we can do the following:
# 
# * Read the file line by line
# * Parse the first line to get a list of the column names or headers
# * Split each remaining line and convert each value into a float
# * Create a dictionary for each loan using the headers as keys
# * Create a list of dictionaries to keep track of all the loans
# 
# Since we will perform the same operations for multiple files, it would be useful to define a function `read_csv`. We'll also define some helper functions to build up the functionality step by step. 
# 
# Let's start by defining a function `parse_header` that takes a line as input and returns a list of column headers.

# In[24]:


def parse_headers(header_line):
    return header_line.strip().split(',')


# The `strip` method removes any extra spaces and the newline character `\n`. The `split` method breaks a string into a list using the given separator (`,` in this case).

# In[25]:


file3_lines[0]


# In[26]:


headers = parse_headers(file3_lines[0])


# In[27]:


headers


# Next, let's define a function `parse_values` that takes a line containing some data and returns a list of floating-point numbers.

# In[28]:


def parse_values(data_line):
    values = []
    for item in data_line.strip().split(','):
        values.append(float(item))
    return values


# In[29]:


file3_lines[1]


# In[30]:


parse_values(file3_lines[1])


# The values were parsed and converted to floating point numbers, as expected. Let's try it for another line from the file, which does not contain a value for the down payment.

# In[31]:


file3_lines[2]


# In[32]:


parse_values(file3_lines[2])


# The code above leads to a `ValueError` because the empty string `''` cannot be converted to a float. We can enhance the `parse_values` function to handle this *edge case*. We will also handle the case where the value is not a float.

# In[33]:


def parse_values(data_line):
    values = []
    for item in data_line.strip().split(','):
        if item == '':
            values.append(0.0)
        else:
            try:
                values.append(float(item))
            except ValueError:
                values.append(item)
    return values


# In[34]:


file3_lines[2]


# In[35]:


parse_values(file3_lines[2])


# Next, let's define a function `create_item_dict` that takes a list of values and a list of headers as inputs and returns a dictionary with the values associated with their respective headers as keys.
# 

# In[36]:


def create_item_dict(values, headers):
    result = {}
    for value, header in zip(values, headers):
        result[header] = value
    return result


# Can you figure out what the Python built-in function `zip` does? Try out an example, or [read the documentation](https://docs.python.org/3.3/library/functions.html#zip).

# In[37]:


for item in zip([1,2,3], ['a', 'b', 'c']):
    print(item)


# Let's try out `create_item_dict` with a couple of examples.

# In[38]:


file3_lines[1]


# In[39]:


values1 = parse_values(file3_lines[1])
create_item_dict(values1, headers)


# In[40]:


file3_lines[2]


# In[41]:


values2 = parse_values(file3_lines[2])
create_item_dict(values2, headers)


# As expected, the values & header are combined to create a dictionary with the appropriate key-value pairs.
# 
# We are now ready to put it all together and define the `read_csv` function.

# In[42]:


def read_csv(path):
    result = []
    # Open the file in read mode
    with open(path, 'r') as f:
        # Get a list of lines
        lines = f.readlines()
        # Parse the header
        headers = parse_headers(lines[0])
        # Loop over the remaining lines
        for data_line in lines[1:]:
            # Parse the values
            values = parse_values(data_line)
            # Create a dictionary using values & headers
            item_dict = create_item_dict(values, headers)
            # Add the dictionary to the result
            result.append(item_dict)
    return result


# Let's try it out!

# In[43]:


with open('./data/loans2.txt') as file2:
    print(file2.read())


# In[44]:


read_csv('./data/loans2.txt')


# The file is read and converted to a list of dictionaries, as expected. The `read_csv` file is generic enough that it can parse any file in the CSV format, with any number of rows or columns. Here's the full code for `read_csv` along with the helper functions:

# In[45]:


def parse_headers(header_line):
    return header_line.strip().split(',')

def parse_values(data_line):
    values = []
    for item in data_line.strip().split(','):
        if item == '':
            values.append(0.0)
        else:
            try:
                values.append(float(item))
            except ValueError:
                values.append(item)
    return values

def create_item_dict(values, headers):
    result = {}
    for value, header in zip(values, headers):
        result[header] = value
    return result

def read_csv(path):
    result = []
    # Open the file in read mode
    with open(path, 'r') as f:
        # Get a list of lines
        lines = f.readlines()
        # Parse the header
        headers = parse_headers(lines[0])
        # Loop over the remaining lines
        for data_line in lines[1:]:
            # Parse the values
            values = parse_values(data_line)
            # Create a dictionary using values & headers
            item_dict = create_item_dict(values, headers)
            # Add the dictionary to the result
            result.append(item_dict)
    return result


# Try to create small, generic, and reusable functions whenever possible. They will likely be useful beyond just the problem at hand and save you significant effort in the future.
# 
# In the [previous tutorial](https://jovian.ml/aakashns/python-functions-and-scope), we defined a function to calculate the equal monthly installments for a loan. Here's what it looked like:

# In[46]:


import math

def loan_emi(amount, duration, rate, down_payment=0):
    """Calculates the equal montly installment (EMI) for a loan.
    
    Arguments:
        amount - Total amount to be spent (loan + down payment)
        duration - Duration of the loan (in months)
        rate - Rate of interest (monthly)
        down_payment (optional) - Optional intial payment (deducted from amount)
    """
    loan_amount = amount - down_payment
    try:
        emi = loan_amount * rate * ((1+rate)**duration) / (((1+rate)**duration)-1)
    except ZeroDivisionError:
        emi = loan_amount / duration
    emi = math.ceil(emi)
    return emi


# We can use this function to calculate EMIs for all the loans in a file.

# In[47]:


loans2 = read_csv('./data/loans2.txt')


# In[48]:


loans2


# In[49]:


for loan in loans2:
    loan['emi'] = loan_emi(loan['amount'], 
                           loan['duration'], 
                           loan['rate']/12, # the CSV contains yearly rates
                           loan['down_payment'])


# In[50]:


loans2


# You can see that each loan now has a new key `emi`, which provides the EMI for the loan. We can extract this logic into a function so that we can use it for other files too.

# In[51]:


def compute_emis(loans):
    for loan in loans:
        loan['emi'] = loan_emi(
            loan['amount'], 
            loan['duration'], 
            loan['rate']/12, # the CSV contains yearly rates
            loan['down_payment'])


# ## Writing to files
# 
# Now that we have performed some processing on the data, it would be good to write the results back to a CSV file. We can create/open a file in `w` mode using `open` and write to it using the `.write` method. The string `format` method will come in handy here.

# In[52]:


loans2 = read_csv('./data/loans2.txt')


# In[53]:


compute_emis(loans2)


# In[54]:


loans2


# In[55]:


with open('./data/emis2.txt', 'w') as f:
    for loan in loans2:
        f.write('{},{},{},{},{}\n'.format(
            loan['amount'], 
            loan['duration'], 
            loan['rate'], 
            loan['down_payment'], 
            loan['emi']))


# Let's verify that the file was created and written to as expected.

# In[56]:


os.listdir('data')


# In[57]:


with open('./data/emis2.txt', 'r') as f:
    print(f.read())


# Great, looks like the loan details (along with the computed EMIs) were written into the file.
# 
# Let's define a generic function `write_csv` which takes a list of dictionaries and writes it to a file in CSV format. We will also include the column headers in the first line.

# In[58]:


def write_csv(items, path):
    # Open the file in write mode
    with open(path, 'w') as f:
        # Return if there's nothing to write
        if len(items) == 0:
            return
        
        # Write the headers in the first line
        headers = list(items[0].keys())
        f.write(','.join(headers) + '\n')
        
        # Write one item per line
        for item in items:
            values = []
            for header in headers:
                values.append(str(item.get(header, "")))
            f.write(','.join(values) + "\n")


# Do you understand how the function works? If now, try executing each statement by line by line or a different cell to figure out how it works. 
# 
# Let's try it out!

# In[59]:


loans3 = read_csv('./data/loans3.txt')


# In[60]:


compute_emis(loans3)


# In[61]:


write_csv(loans3, './data/emis3.txt')


# In[62]:


with open('./data/emis3.txt', 'r') as f:
    print(f.read())


# With just four lines of code, we can now read each downloaded file, calculate the EMIs, and write the results back to new files:

# In[63]:


for i in range(1,4):
    loans = read_csv('./data/loans{}.txt'.format(i))
    compute_emis(loans)
    write_csv(loans, './data/emis{}.txt'.format(i))


# In[64]:


os.listdir('./data')


# Isn't that wonderful? Once all the functions are defined, we can calculate EMIs for thousands or even millions of loans across many files in seconds with just a few lines of code. Now we're starting to see the real power of using a programming language like Python for processing data!

# ## Using Pandas to Read and Write CSVs
# 
# There are some limitations to the `read_csv` and `write_csv` functions we've defined above:
# 
# * The `read_csv` function fails to create a proper dictionary if any of the values in the CSV files contains commas
# * The `write_csv` function fails to create a proper CSV if any of the values to be written contains commas
# 
# When a value in a CSV file contains a comma (`,`), the value is generally placed within double quotes. Double quotes (`"`) in values are converted into two double quotes (`""`). Here's an example:
# 
# ```
# title,description
# Fast & Furious,"A movie, a race, a franchise"
# The Dark Knight,"Gotham, the ""Batman"", and the Joker"
# Memento,A guy forgets everything every 15 minutes
# 
# ```
# 
# Let's try it out.

# In[65]:


movies_url = "https://gist.githubusercontent.com/aakashns/afee0a407d44bbc02321993548021af9/raw/6d7473f0ac4c54aca65fc4b06ed831b8a4840190/movies.csv"


# In[66]:


urlretrieve(movies_url, 'data/movies.csv')


# In[67]:


movies = read_csv('data/movies.csv')


# In[68]:


movies


# As you can seen above, the movie descriptions weren't parsed properly.
# 
# To read this CSV properly, we can use the `pandas` library.

# In[69]:


get_ipython().system('pip install pandas --upgrade --quiet')


# In[70]:


import pandas as pd


# The `pd.read_csv` function can be used to read the CSV file into a pandas data frame: a spreadsheet-like object for analyzing and processing data. We'll learn more about data frames in a future lesson.

# In[71]:


movies_dataframe = pd.read_csv('data/movies.csv')


# In[72]:


movies_dataframe


# A dataframe can be converted into a list of dictionaries using the `to_dict` method.

# In[73]:


movies = movies_dataframe.to_dict('records')


# In[74]:


movies


# If you don't pass the arguments `records`, you get a dictionary of lists instead.

# In[75]:


movies_dict = movies_dataframe.to_dict()


# In[76]:


movies_dict


# Let's try using the `write_csv` function to write the data in `movies` back to a CSV file.

# In[77]:


write_csv(movies, 'movies2.csv')


# In[78]:


get_ipython().system('head movies2.csv')


# As you can see above, the CSV file is not formatted properly. This can be verified by attempting to read the file using `pd.read_csv`.

# In[79]:


pd.read_csv('movies2.csv')


# To convert a list of dictionaries into a dataframe, you can use the `pd.DataFrame` constructor.

# In[80]:


df2 = pd.DataFrame(movies)


# In[81]:


df2


# It can now be written to a CSV file using the `.to_csv` method of a dataframe.

# In[82]:


df2.to_csv('movies3.csv', index=None)


# Can you guess what the argument `index=None` does? Try removing it and observing the difference in output.

# In[83]:


get_ipython().system('head movies3.csv')


# The CSV file is formatted properly. We can verify this by trying to read it back.

# In[84]:


pd.read_csv('movies3.csv')


# We're able to write and read the file properly with `pandas`. 
# 
# In general, it's always a better idea to use libraries like Pandas for reading and writing CSV files. 

# ### Save and upload your notebook
# 
# Whether you're running this Jupyter notebook online or on your computer, it's essential to save your work from time to time. You can continue working on a saved notebook later or share it with friends and colleagues to let them execute your code. [Jovian](https://www.jovian.ai) offers an easy way of saving and sharing your Jupyter notebooks online.

# In[85]:


# Install the library
get_ipython().system('pip install jovian --upgrade --quiet')


# In[86]:


# Import the jovian module
import jovian


# In[ ]:


jovian.commit(project='python-os-and-filesystem')


# The first time you run `jovian.commit`, you'll be asked to provide an API Key to securely upload the notebook to your Jovian account. You can get the API key from your [Jovian profile page](https://jovian.ai) after logging in / signing up.
# 
# 
# `jovian.commit` uploads the notebook to your Jovian account, captures the Python environment, and creates a shareable link for your notebook, as shown above. You can use this link to share your work and let anyone (including you) run your notebooks and reproduce your work.

# ## Exercise - Processing CSV files using a dictionary of lists
# 
# We defined the functions `read_csv` and `write_csv` above to convert a CSV file into a list of dictionaries and vice versa. In this exercise, you'll transform the CSV data into a dictionary of lists instead, with one list for each column in the file.
# 
# For example, consider the following CSV file:
# 
# ```
# amount,duration,rate,down_payment
# 828400,120,0.11,100000
# 4633400,240,0.06,
# 42900,90,0.08,8900
# 983000,16,0.14,
# 15230,48,0.07,4300
# ```
# 
# We'll convert it into the following dictionary of lists:
# 
# ```
# {
#   amount: [828400, 4633400, 42900, 983000, 15230],
#   duration: []120, 240, 90, 16, 48],
#   rate: [0.11, 0.06, 0.08, 0.14, 0.07],
#   down_payment: [100000, 0, 8900, 0, 4300]
# }
# ```
# 
# Complete the following tasks using the empty cells below:
# 
# 1. Download three CSV files to the folder `data2` using the URLs listed in the code cell below, and verify the downloaded files.
# 2. Define a function `read_csv_columnar` that reads a CSV file and returns a dictionary of lists in the format shown above. 
# 3. Define a function `compute_emis` that adds another key `emi` into the dictionary with a list of EMIs computed for each row of data.
# 4. Define a function `write_csv_columnar` that writes the data from the dictionary of lists into a correctly formatted CSV file.
# 5. Process all three downloaded files and write the results by creating new files in the directory `data2`.
# 
# Define helper functions wherever required.
# 

# In[ ]:


url1 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans1.txt'
url2 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans2.txt'
url3 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans3.txt'


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# Finally, let's save a snapshot of our work using `jovian.commit`.

# In[ ]:


jovian.commit(project='python-os-and-filesystem')


# ## Summary and Further Reading
# 
# With this, we complete our discussion of reading from and writing to files in Python. We've covered the following topics in this tutorial:
# 
# * Interacting with the file system using the `os` module
# * Downloading files from URLs using the `urllib` module
# * Opening files using the `open` built-in function
# * Reading the contents of a file using `.read`
# * Closing a file automatically using `with`
# * Reading a file line by line using `readlines`
# * Processing data from a CSV file by defining functions
# * Using helper functions to build more complex functions
# * Writing data to a file using `.write`
# 
# This tutorial on working with files in Python is by no means exhaustive. Following are some more resources you should check out:
# 
# * Python Tutorial at W3Schools: https://www.w3schools.com/python/
# * Practical Python Programming: https://dabeaz-course.github.io/practical-python/Notes/Contents.html
# * Python official documentation: https://docs.python.org/3/tutorial/index.html
# 
# You are ready to move on to the next tutorial: [Numerical Computing with Python and Numpy](https://jovian.ai/aakashns/python-numerical-computing-with-numpy).

# In[ ]:




