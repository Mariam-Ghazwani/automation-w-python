x = ["Now", "we", "are", "cooking!"]
type (x)
print(x)
len(x)
print(x[0])
print(x[3])


def group_list(group, users):
  members = group + ": " + ", ".join(users)
  return members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

# Modifying the Contents of a List
fruits.append("Kiwi")
fruits.insert(0,"Orange")
fruits.remove("Melon")
fruits.pop(3)
# to modify/change/replace the element in the list
fruits[2] = "Strawberry"

# List Comprehensions - let us create new lists based on swquences or ranges
multiples = [ x*7 for x in range(1,11)]
print(multiples)

#
languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print (lenghts)

z = [x for x in range(0,101) if x % 3 == 0]
print(z)

# return every other element from the list, this time using a list comprehension to generate the new list
# based on the previous one, where elements in odd positions are skipped.

def skip_elements(elements):
	return [ element for element in elements if index % 2 == 0]  

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

# rename all the files with extension hpp to the extension h.
# To do this, we would like to generate a new list called newfilenames, consisting of the new filenames.
# Fill in the blanks in the code using any of the methods you’ve learned thus far, like a for loop or a list comprehension.

filenames = ["program.c", "stdio.hpp",
             "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
old_ext = "hpp"
new_ext = "h"
newfilenames = []
for name in filenames:
    if "." + old_ext in name:
        index = name.index("." + old_ext)
        newfilenames.append(name[:index] + "." + new_ext)
    else:
        newfilenames.append(name)
print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


# The permissions of a file in a Linux system are split into three sets of three permissions: read, write, 
# and execute for the owner, group, and others. Each of the three values can be expressed as an octal number 
# summing each permission, with 4 corresponding to read, 2 to write, and 1 to execute. Or it can be written 
# with a string using the letters r, w, and x or - when the permission is not granted. For example: 640 is 
# read/write for the owner, read for the group, and no permissions for the others; converted to a string, it 
# would be: "rw-r-----" 755 is read/write/execute for the owner, and read/execute for group and others; 
# converted to a string, it would be: "rwxr-xr-x" Fill in the blanks to make the code convert a permission 
# in octal format into a string format.

def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for digit in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if digit >= value:
                result += letter
                digit -= value
            else:
                result += "-"
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------


# Create a function that turns text into pig latin: a simple text 
# transformation that modifies each word moving the first character 
# to the end and appending "ay" to the end. For example, python ends 
# up as ythonpay.

def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split
for word in words:
    # Create the pig latin word and add it to the list
    pigword = 
    # Turn the list back into a phrase
  return ___
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"