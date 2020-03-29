def guest_list(guests):
	for guest in guests:
		name, age, pro = guest
		print("{name} is {age} years old and works as {pro}.".format(name=name, age=age, pro=pro))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#
animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
	chars += len(animal)
print("Total characters: {}, Average lenght: {}".format(chars, chars/len(animals)))
#

winners = ["Ashely", "Dylan", "Reese"]
for index, person in enumerate(winners):
	print("{} - {}".format(index + 1, person))


def skip_elements(elements):
    new = []
    if elements != "":
        for index, element in enumerate(elements):
            if index % 2 == 0:
                new.append("{}".format(element))
    return new

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

def full_emails(people):
	# people is a list of tuples, 2 strings each. The first element is the email address and the second one is the full name.
	result = []
	for email, name in people:
		result.append("{} <{}>".format(name,email))
	return result

print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brant")]))
