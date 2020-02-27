def double_word(word):
  dw = word * 2
  return dw + str(len(dw))

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0

message = "A kong string with a silly typo"
new_message = message[0:2] + "l" + message[3:]

word = "supercalifragilisticexpialidocious"
print(word.index("x"))

def replace_domain(email, old_domain, new_domain):
  if "@" + old_domain in email:
    index = email.index("@" + old_domain)
    new_email = email[:index] + "@" + new_domain
    return new_email
  return email

def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0]
    return result.upper()

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS

name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name,number))
# Because we're using placeholders with variable names, the order in which 
# the variables are passed to the format function doesn't matter. But for this to work, 
# we need to set the names we're going to use and assign a value to them inside the parameters to format. 
print ("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*3))

def student_grade(name, grade):
	return "{name} received {grade}% on the exam".format(name=name, grade=grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

#Formatting expression
price = 7.5
with_tax = price * 1.09
print (price, with_tax)

print ("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))

def to_celsius(x):
  return (x-32)*5/9

for x in range (0,101,10)
  print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))

''' String Reference Cheat Sheet
In Python, there are a lot of things you can do with strings. In this cheat sheet, you’ll find the most common string operations and string methods.

String operations
len(string) Returns the length of the string
for character in string Iterates over each character in the string
if substring in string Checks whether the substring is part of the string
string[i] Accesses the character at index i of the string, starting at zero
string[i:j] Accesses the substring starting at index i, ending at index j-1. If i is omitted, it's 0 by default. If j is omitted, it's len(string) by default.

String methods
string.lower() / string.upper() Returns a copy of the string with all lower / upper case characters
string.lstrip() / string.rstrip() / string.strip() Returns a copy of the string without left / right / left or right whitespace
string.count(substring) Returns the number of times substring is present in the string
string.isnumeric() Returns True if there are only numeric characters in the string. If not, returns False.
string.isalpha() Returns True if there are only alphabetic characters in the string. If not, returns False.
string.split() / string.split(delimiter) Returns a list of substrings that were separated by whitespace / delimiter
string.replace(old, new) Returns a new string where all occurrences of old have been replaced by new.
delimiter.join(list of strings) Returns a new string with all the strings joined by the delimiter '''

def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	letter = ""
	for letter in input_string:
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string.
		if letter is not " ":
			new_string = new_string + letter
			reverse_string = letter+reverse_string
	# Compare the strings
	if new_string.lower() == reverse_string.lower():
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True

def convert_distance(miles):
	km = miles * 1.6 
	result = "{} miles equals {:.1f} km".format(miles,km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km
