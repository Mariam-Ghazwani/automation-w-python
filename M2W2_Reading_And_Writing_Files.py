# Module 2 Week 2 | Reading Files

file = open("spider.txt")
print(file.readline()) #reads one line from current position

print(file.read()) #reads from current position to files end

file.close() #file is locked until not closed

with open("spidter.txt") as file:
    print(file.readline())
# using with block will have file closed 

with open("spider.txt") as file:
    for line in file:
        print(line.upper())
# this will print out file line by line making each line UPERCASE before printing

with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())
#this will get output without empty lines (strip methid clears spaces, tabs and new line characters)

file = open("spider.txt")
lines =  file.readline() # lines will now have all the content of spider.txt
file.colse()
lines.sort()
print(lines)

# Module 2 Week 2 | Writing Files

with open("novel.txt", "w") as file:
    file.write("It is what it is") #will return count of caracter written in file
# "r" mode is read mode, this is default mode and doesn't need to be specified
# "w" will override all contents if file exists, cannot read file, if the file doesn't exist the Python will crreate it
# "a" will append contents at the end of the existing file
# "r+" read-write


## Practice Notebook: Reading and Writing Files

# In this exercise, we will test your knowledge of reading and writing files by playing around with some text files. 
# 
# Let's say we have a text file containing current visitors at a hotel.  We'll call it, *guests.txt*.  
# Run the following code to create the file.  The file will automatically populate with each initial guest's first name on its own line.

# In[1]:


guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")
    
guests.close()


# No output is generated for the above code cell.  To check the contents of the newly created *guests.txt* file, run the following code.

# In[2]:


with open("guests.txt") as guests:
    for line in guests:
        print(line)


# The output shows that our *guests.txt* file is correctly populated with each initial guest's first name on its own line.  Cool!
# <br><br>
# Now suppose we want to update our file as guests check in and out.  Fill in the missing code in the following cell to add guests to the *guests.txt* file as they check in.

# In[5]:


new_guests = ["Sam", "Danielle", "Jacob"]

with open("guests.txt","a") as guests:
    for i in new_guests:
        guests.write(i + "\n")

guests.close()


# To check whether your code correctly added the new guests to the *guests.txt* file, run the following cell.

# In[6]:


with open("guests.txt") as guests:
    for line in guests:
        print(line)


# The current names in the *guests.txt* file should be:  Bob, Andrea, Manuel, Polly, Khalid, Sam, Danielle and Jacob.
# <br><br>
# Was the *guests.txt* file correctly appended with the new guests? If not, go back and edit your code making sure to fill in the gaps appropriately so that the new guests are correctly added to the *guests.txt* file.  Once the new guests are successfully added, you have filled in the missing code correctly.  Great!
# <br><br>
# Now let's remove the guests that have checked out already.  There are several ways to do this, however, the method we will choose for this exercise is outlined as follows:
# 1. Open the file in "read" mode.
# 2. Iterate over each line in the file and put each guest's name into a Python list.
# 3. Open the file once again in "write" mode.
# 4. Add each guest's name in the Python list to the file one by one.
# 
# <br>
# Ready? Fill in the missing code in the following cell to remove the guests that have checked out already.

# In[7]:


checked_out=["Andrea", "Manuel", "Khalid"]
temp_list=[]

with open("guests.txt", "r") as guests:
    for g in guests:
        temp_list.append(g.strip())

with open("guests.txt", "w") as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name + "\n")


# To check whether your code correctly removed the checked out guests from the *guests.txt* file, run the following cell.

# In[8]:


with open("guests.txt") as guests:
    for line in guests:
        print(line)


# The current names in the *guests.txt* file should be:  Bob, Polly, Sam, Danielle and Jacob.
# <br><br>
# Were the names of the checked out guests correctly removed from the *guests.txt* file? If not, go back and edit your code making sure to fill in the gaps appropriately so that the checked out guests are correctly removed from the *guests.txt* file. Once the checked out guests are successfully removed, you have filled in the missing code correctly. Awesome!
# <br><br>
# Now let's check whether Bob and Andrea are still checked in.  How could we do this? We'll just read through each line in the file to see if their name is in there.  Run the following code to check whether Bob and Andrea are still checked in.

# In[9]:


guests_to_check = ['Bob', 'Andrea']
checked_in = []

with open("guests.txt","r") as guests:
    for g in guests:
        checked_in.append(g.strip())
    for check in guests_to_check:
        if check in checked_in:
            print("{} is checked in".format(check))
        else:
            print("{} is not checked in".format(check))


# We can see that Bob is checked in while Andrea is not.  Nice work! You've learned the basics of reading and writing files in Python!


# os module usage

import os
#Remove function using OS module
os.remove("novel.txt")
#Rename function old name then new name of a file
os.rename("first_draft.txt", "finished_masterpiece.txt")

# os.path sub-module in OS module
os.path.extsts("finished_masterpiece.txt")

# os.path.getsize returns the filesize in bytes
os.path.getsize("finished_masterpiece.txt")

# os.path.getmtime returns unix timestamp for file when it was last modified 
os.path.getmtime"finished_masterpiece.txt")

import datetime
timestamp  = os.path.getmtime("spider.txt")
datetime.datetime.fromtimestamp(timestamp)
#retuns:
# datetime.datetime(2020,1,6,7,2,3, 8999999)

import os
file= "file.dat"
if os.path.isfile(file):
    print(os.path.isfile(file))
    print(os.path.getsize(file))
else:
	print(os.path.isfile(file))
    print("File not found")

# The abspath function takes a filename and turns it into an absolute path.
# Python uses the current working directory which is where the script is being 
# run to start looking for the file and construct the full path that identifies it. 
# This is useful if you want to store at the file's full path or access a file no matter 
# what the current directory is. 
os.path.abspath("spider.txt")

# To check which current directory your Python program is 
# executing in, you can use the getcwd method.
print(os.getcwd())
# create directory
os.mkdir("new_dir")
# change directories 
os.chdir("new_dir")
os.getcwd()

os.mkdir("newer_dir")
os.rmdir("newer_dir") #rmdir will only work if dir is empty

# The os.listdir function returns a list of all the files and sub-directories in a given directory.
os.listdir("website")
# returns filenimes which are strings
# Since they're just strings, we don't know if they're directories or files.
# If we want to know whether one of these files is a directory, 
# we need to use os.path.join to create the full path.
dir = "website"
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))
# By using os.path.join we can concatenate directories in a
# way that can be used with other os.path() functions.

# QUIZ 

# The create_python_script function creates a new python script in the current 
# working directory, adds the line of comments to it declared by the 'comments' 
# variable, and returns the size of the new file. Fill in the gaps to create 
# a script called "program.py".
import os
def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, "w") as file:
    file.write(comments)
  filesize = os.path.getsize(filename)
  return(filesize)

print(create_python_script("program.py"))

# The new_directory function creates a new directory inside the current working directory, 
# then creates a new empty file inside the new directory, and returns the list of files in 
# that directory. Fill in the gaps to create a file "script.py" in the directory "PythonPrograms".

import os
def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  # then create a directory
  if os.path.isdir(directory) == False:
    # print("Making Dir: ", os.listdir)
    os.mkdir(directory)
  # Create the new file inside of the new directory
  with open(os.path.join(directory, filename), "w") as file:
    pass
  # Return the list of files in the new directory

  return os.listdir(directory)
print(new_directory("PythonPrograms", "script.py"))

# The file_date function creates a new file in the current working directory, 
# checks the date that the file was modified, and returns just the date portion of 
# the timestamp in the format of yyyy-mm-dd. Fill in the gaps to create a file 
# called "newfile.txt" and check the date that it was modified.

import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename, "w") as file:
    timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  date = datetime.datetime.fromtimestamp(timestamp)
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{:%Y-%m-%d}".format(date))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd

# The parent_directory function returns the name of the directory that's located just above 
# the current working directory. Remember that '..' is a relative path alias that means 
# "go up to the parent directory". Fill in the gaps to complete this function.

import os
def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory
  path = "../"
  relative_parent = os.path.join(os.getcwd(), path)

  # Return the absolute path of the parent directory
  return os.path.abspath(relative_parent)

print(parent_directory())


import os
def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory
  path = "../"
  #relative_parent = os.path.join(os.getcwd(), path)

  # Return the absolute path of the parent directory
  return os.path.abspath(path)

print(parent_directory())

# CSV files
# Reading CSV Files

import csv
f = open("csv_file.txt")
csv_f = csv.reader(f) # The reader() function of the CSV module will interpret the file as a CSV.
for row in csv_f:
    name, phone, role = row
    print("Nem: {}, Phone: {}, Role: {}".format(name, phone, role))
f.close()



# Generating CSV

# We unpack the row so that we don't have to use indexes to access each element in that list. 
# For example, we could have used row[0] to access the name of the employee. 
# This is valid but it can be hard to follow when reading a lot of code. 
# Unpacking the list into name variables makes the code easier to understand later on. 
# And before we forget, let's close this file now that we're done with it.

hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]
# The file must be open, preferably using with open() as, and write permissions must be given
# before using the csv.writer() function
with open('hosts.csv', 'w') as hosts_csv:
  writer = csv.writer(hosts_csv)
  writer.writerows(hosts)


# Reading and Writing CSV Files with Dictionaries

with open('software.csv') as software:
# DictReader turns each row of the data in a CSV file into a dictionary.
# We can then access the data by using the column names instead of the position in the row.
  reader = csv.DictReader(software)
  for row in reader:
    print (("{} has {} users").format(row["name"], row["users"]))

users = [ {"name": "Sol Mansi", "username": "slom", "department": "IT infrastructure"}, 
{"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
{"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "deprtment"] #define the list of keys that we want to write to the file

with open ('by_department.csv', 'w') as by_department: #open the file for writing
  writer = csv.DictWriter(by_department, fieldnames=keys) #create the DictWriter passing the keys that we had identified before
  writer.writehead() #the writeheader method will create the first line of the CSV based on keys that we passed
  writer.writerows(users) #the writerows method will turn the list of dictionaries into lines in that file

>>> user@ubumntu:~$ cat by_department.csv

# Practice Quiz: Reading & Writing CSV Files

# 1
# We're working with a list of flowers and some information about each one. 
# The create_file function writes this information to a CSV file. 
# The contents_of_file function reads this file into records and returns the information in a nicely formatted block. 
# Fill in the gaps of the contents_of_file function to turn the data in the CSV file into a dictionary using DictReader.

import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename) as file:
    # Read the rows of the file into a dictionary
    reader = csv.DictReader(file)
    # Process each item of the dictionary
    for row in reader:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))

# 2
# Using the CSV file of flowers again, fill in the gaps of the contents_of_file function to 
# process the data without turning it into a dictionary. 
# How do you skip over the header record with the field names?

import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename) as file:
    # Read the rows of the file
    rows = csv.reader(file)
    # Process each row
    next (file) # to skip the first line
    for row in rows:
      name, color, typ = row
      # Format the return string for data rows only
      return_string += "a {} {} is {}\n".format(color, name, typ)
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))