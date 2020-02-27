# The skip_elements function returns every other element from the list, starting from the first. Complete this function to do that.

def skip_elements(elements):
	# code goes here
	e = len(elements) - 1
	# print("Elementi Total -1: ",e)
	if elements != "":
	  for x in range(1,e,2):
	    # print ("Len:",e," x=",x, "Index: ",e-x)
	    elements.pop(e-x)
	  return elements

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []
print(skip_elements(['Elina', 'Aldis', 'Peteris', 'Ieva', 'Ernests', 'Patriks', 'Olivers']))