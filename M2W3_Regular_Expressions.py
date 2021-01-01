
# Regular Expressions
# Regular expressions allow us to search a text for strings matching a specific pattern. 
# Besides Python and other programming languages we can  also use command line tools that know how to apply regexs, like grep, sed, or awk.

import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"

# with string methods:
index = log.index("[")
print(log[index+1:index+6])

# using regex:
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

# Basic Matching with grep

CLI: grep thon /usr/share/dict/words

# pass the -i parameter to the grep to match a string regardless of case
CLI: grep -i python /usr/share/dict/words 

# a dot matches any character
grep s.ing /usr/share/dict/words

# ^ indicates the beginning
grep ^fruit /usr/share/dict/words

# & indicates the end
grep cat$ /usr/share/dict/words

## Simple Matching in Python
import re

# The r at the beginning of the pattern indicates that this is a rawstring.
# This means that Python interpreter shouldn't try to interpret any special 
# characters, and instead, should just pass the string to the function as is. 
# In this example, there are no special characters. 
result = re.search(r"aza", "plaza")
print (result)
<re.Match object: span=(2,5), match='aza'>

print(re.search(r"^x", "xenon"))

print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))


# Fill in the code to check if the text passed contains the vowels a, e and i,
# with exactly one occurrence of any other character in between.

import re
def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True

## Wildcards and Character Classes
# Character classes are written inside square brackets and let us list the characters we want to match inside of those brackets.

print(re.search(r"[Pp]ython", "Python"))

print(re.search(r"[a-z]way", "The end of the highway"))
match='hway'
print(re.search(r"[a-z]way", "What a way to go"))
match None
print(re.search(r"cloud[a-zA-Z0-9]", "cloudy9"))
match cloudy9

# Fill in the code to check if the text passed contains punctuation symbols:
# commas, periods, colons, semicolons, question marks, and exclamation points.

import re
def check_punctuation (text):
  result = re.search(r"[a-zA-Z][,.!?:;]$", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False

# search pattern that looks for any characters that's not a letter
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces.")) 
match=' ' span=(4, 5) # match is the first space character
# add spaces to include SPACE as character that we don't want to match
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces.")) 
match='.' span=(30, 31) # match is the first space character

# Use | pipe symbol to match either one expression or another. This lets us list alternative options that can get matched.
print(re.search(r"cat|dog", "I like cats.")) 
match='cat' span=(7, 10) 

print(re.findall(r"cat|dog", "I like both dogs and cats.")) 
match='dog','cat'

## Repetition Qualifiers

# Here we match Py followed by any number of other characters followed by n. But with our dot star combination we expanded the range of the match to the whole word. 
print(re.search(r"Pyt*n", "Pygmalion")) 
match='Pygmalion'
# Star * character takes as many characters as possible. In programming terms, we say that this behavior is greedy.
print(re.search(r"Pyt*n", "Python Programming")) 
match='Python Programming'
# for pattern to only match letters we need to use character class instead
print(re.search(r"Py[a-z]*n", "Python Programming")) 
match='Python Programming'
# it will also match "0"/zero times:
print(re.search(r"Py[a-z]*n", "Pyn")) 
match='Pyn'
# The plus character matches one or more occurrences of the character that comes before it:
print(re.search(r"o+l+", "goldfish")) 
match='ol'
print(re.search(r"o+l+", "woolly")) 
match='ooll'

# The repeating_letter_a function checks if the text passed includes the letter "a" (lowercase or uppercase) at least twice.
# For example, repeating_letter_a("banana") is True, while repeating_letter_a("pineapple") is False.
# Fill in the code to make this work. 

import re
def repeating_letter_a(text):
  result = re.search(r"[aA].*[aA]", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True

# The question mark symbol is yet another multiplier.
# It means either zero or one occurrence of the character before it.
print(re.search(r"p?each", "To each their own")) 
match='each'
print(re.search(r"p?each", "I like peaches")) 
match='peach'

# Escaping Characters
print(re.search(r".com", "welcome")) 
match='lcom'
print(re.search(r"\.com", "welcome")) 
match = None
print(re.search(r"\.com", "mydoman.com")) 
match ='.com'
# \w matches any alphanumeric character including letters, numbers, and underscores (but not spaces)
print(re.search(r"\w*", "This is an example")) 
match ='This'
print(re.search(r"\w*", "And_this_is_another")) 
match ='And_this_is_another'
# there is also \d for matching digits, \s for matching whitespace characters like space, tab or new line, \b for word boundaries and a few others

# Fill in the code to check if the text passed has at least 2 groups of alphanumeric characters
# (including letters, numbers, and underscores) separated by one or more whitespace characters.
import re
def check_character_groups(text):
  result = re.search(r"\w\s", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False

# Regular Expressions in Action
print(re.search(r"^A.*a$", "Australia")) 
match ='Australia'

# Using regular expressions, we can also construct a pattern that would validate if the string is a valid variable name in Python.
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
match ='_this_is_a_valid_variable_name'

# Fill in the code to check if the text passed looks like a standard sentence, 
# meaning that it starts with an uppercase letter, followed by at least some 
# lowercase letters or a space, and ends with a period, question mark, or exclamation point. 
import re
def check_sentence(text):
  result = re.search(r"^[A-Z][a-z ]*[\.?!]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True

## Practice Quiz: Basic Regular Expressions

# The check_web_address function checks if the text passed qualifies as a top-level web address, 
# meaning that it contains alphanumeric characters (which includes letters, numbers, and underscores), 
# as well as periods, dashes, and a plus sign, followed by a period and a character-only top-level 
# domain such as ".com", ".info", ".edu", etc. Fill in the regular expression to do that, using escape 
# characters, wildcards, repetition qualifiers, beginning and end-of-line characters, and character classes.

import re
def check_web_address(text):
  pattern = r"[\.][A-Za-z]*$"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True

# The check_time function checks for the time format of a 12-hour clock, as follows: 
# the hour is between 1 and 12, with no leading zero, followed by a colon, then minutes 
# between 00 and 59, then an optional space, and then AM or PM, in upper or lower case. 
# Fill in the regular expression to do that. How many of the concepts that you just learned can you use here?

import re
def check_time(text):
  pattern = r"[1-9]+:\d[1-9]\s*[Aa]|[Pp][Mm]"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False

# The contains_acronym function checks the text for the presence of 2 or more characters or digits surrounded by parentheses, 
# with at least the first character in uppercase (if it's a letter), returning True if the condition is met, or False otherwise. 
# For example, "Instant messaging (IM) is a set of communication technologies used for text-based communication" 
# should return True since (IM) satisfies the match conditions." Fill in the regular expression in this function: 

import re
def contains_acronym(text):
  pattern = ___ 
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True

# Fill in the code to check if the text passed includes a possible U.S. zip code, formatted as follows: 
# exactly 5 digits, and sometimes, but not always, followed by a dash with 4 more digits. 
# The zip code needs to be preceded by at least one space, and cannot be at the start of the text.

import re
def check_zip_code (text):
  result = re.search(r".* [0-9]{5}", text)
  return result != None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False


# Advanced Regular Expressions
# Capturing Groups

result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
# match = 'Lovelace, Ada)
print(result.groups()
('Lovelace', 'Ada') # Because we defined two separate groups, the group method returns a tuple of two elements.
print(result[0])
Lovelace, Ada
"{} {}".format(result[2], result[1])
'Ada Lovelace'

def rearrange_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])

# More on Repetition Qualifiers
print(re.search(r"[a-zA-Z]{5}", "a ghost"))
match = 'ghost'
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))
match = ['scary', 'ghost', 'appea']
# if we wanted to match all the words that are exactly five letters long? We can do that using \b, which matches word limits
#  at the beginning and end of the pattern, to indicate that we want full words
print(re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared"))
match = ['scary', 'ghost']
# if we wanted to match a range of five to ten letters or numbers, we could use an expression like this one:
print(re.findall(r"\w{5,10}", "I really like strawberries"))
match = ['really', 'strawberri']
print(re.findall(r"\w{5,}", "I really like strawberries"))
match = ['really', 'strawberries']
# Here we look for a pattern that was an S followed by up to 20 alphanumeric characters.
print(re.search(r"s\w{","20}", "I really like strawberries"))
match = ['strawberries']

# More on Repetition Qualifiers task
# The long_words function returns all words that are at least 7 characters. Fill in the regular expression to complete this function.

import re
def long_words(text):
  pattern = r"\w{7,}"
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []

# Extracting a PID Using regexes in Python

import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]" '''After the square bracket, comes the first parentheses. Since it isn't escaped, we know it'll be used as a capturing group. 
The capturing group parentheses are wrapping the backslash d+ symbols. From our discussion of special characters and repetition qualifiers, 
we know that this expression will match one or more numerical characters.'''
result = re.search(regex, log)
print(result[1]) # After calling the search function, we know that because we're capturing groups in an expression, we can access the matching data by accessing the value at index 1. 

# We should have a function that extracts the process ID or PID when possible, and does something else if not. It's something like this; will start by defining a function called extract_pid.

import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"

def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]

print(extract_pid(log))

# Question/task
# Add to the regular expression used in the extract_pid function, to return the uppercase message in parenthesis, after the process id.
import re
def extract_pid(log_line):
    regex = r"(\[(\d+)\]).*\s([A-Z]*)\s"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[2], result[3])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)

# Splitting and Replacing
re.split(r"[.?!]", "One sentence. Another one? And the last one!")
['One sentence', 'Another one', 'And the last one', '']
re.split(r"([.?!])", "One sentence. Another one? And the last one!")
['One sentence', '.', 'Another one', '?', 'And the last one', '!', '']

# Another interesting function provided by the RE module is called sub.
# It's used for creating new strings by substituting all or part of them for a different string, 
# similar to the replace string method but using regular expressions for both the matching and the replacing.

re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com")
Received an email for [REDACTED]

re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")
'Ada Lovelace''


# If we want to make sure that only the actual words are used to split the text, we need to use the escape character 
# or word boundaries, like this: r"\bthe\b|\ba\b". Otherwise, any instance of the given words is used as delimiters, 
# no matter where they are in the text, even in the middle of other words like "Another" and "last".

re.split(r"the|a", "One sentence. Another one? And the last one!")
['One sentence. Ano', 'r one? And ', ' l', 'st one!']

# Practice Quiz: Advanced Regular Expressions
# 1
# We're working with a CSV file, which contains employee information. Each record has a name field, followed by a phone 
# number field, and a role field. The phone number field contains U.S. phone numbers, and needs to be modified to the 
# international format, with "+1-" in front of the phone number. Fill in the regular expression, using groups, to use 
# the transform_record function to do that.

import re
def transform_record(record):
  new_record = re.sub(r"(\d{3}-\d{3}-?\d{4})", r"+1-\1", record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer


# 2
# The multi_vowel_words function returns all words with 3 or more consecutive vowels (a, e, i, o, u). Fill in the regular expression to do that.

import re
def multi_vowel_words(text):
  pattern = r"(\w*[aeiou]{3}\w*)"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []

# 3
# The transform_comments function converts comments in a Python script into those usable by a C compiler. 
# This means looking for text that begins with a hash mark (#) and replacing it with double slashes (//), 
# which is the C single-line comment indicator. For the purpose of this exercise, we'll ignore the possibility 
# of a hash mark embedded inside of a Python command, and assume that it's only used to indicate a comment. 
# We also want to treat repetitive hash marks (##), (###), etc., as a single comment indicator, to be 
# eplaced with just (//) and not (#//) or (//#). Fill in the parameters of the substitution method to complete this function: 

import re
def transform_comments(line_of_code):
  result = re.sub(r"#+", r"//", line_of_code)
  return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"

# 4
# The convert_phone_number function checks for a U.S. phone number format: XXX-XXX-XXXX 
# (3 digits followed by a dash, 3 more digits followed by a dash, and 4 digits), and 
# converts it to a more formal format that looks like this: (XXX) XXX-XXXX. 
# Fill in the regular expression to complete this function.

import re
def convert_phone_number(phone):
  result = re.sub(r"(\d{3})-(\d{3}-\d{4}\b)", r"(\1) \2", phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300

