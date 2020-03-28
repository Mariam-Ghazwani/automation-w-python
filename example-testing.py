def skip_elements(elements):
	# code goes here
	e = len(elements)
	print("elementi: ",e)
	if elements != "":
	  for x in range(1,e,2):
	    print (elements[x])
	    elements.pop(x)
	  return elements

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []