def guest_list(guests):
	for guest in guests:
		name, age, pro = guest
		print("{name} is {age} years old and works as {pro}.".format(name=name, age=age, pro=pro))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

