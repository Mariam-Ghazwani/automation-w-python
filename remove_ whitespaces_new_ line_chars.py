#remove whitespaces and new line chars from the String

def clean_string(input_string):
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