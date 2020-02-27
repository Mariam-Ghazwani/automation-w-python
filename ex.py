def skip_elements(elements):
	# code goes here
	e = len(elements)
	print("Elementi TOTAL: ",e)
	if elements != "":
	  for x in range(e):
	    print (e,x+1)
	    elements.pop(e-(x+1))
	  return elements

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []