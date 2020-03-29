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