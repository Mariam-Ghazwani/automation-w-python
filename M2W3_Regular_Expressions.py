
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
  pattern = ___
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True