class Flower():
  color = 'unknown'

rose = Flower()
rose.color = "red"

violet = Flower()
violet.color = "blue"

this_pun_is_for_you = '''Wine costs less
than Dinner for Two'''

print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))
print(this_pun_is_for_you) 

Let’s test your knowledge of using dot notation to access methods and attributes in an object. 
Let’s say we have a class called Birds. Birds has two attributes: color and number. 
Birds also has a method called count() that counts the number of birds (adds a value to number). 
Which of the following lines of code will correctly print the number of birds? Keep in mind, 
the number of birds is 0 until they are counted!

bluejay.count()
print(bluejay.number)

# Creating new instances of class objects can be a great way to keep track of values using attributes associated with the object. 
# The values of these attributes can be easily changed at the object level. 
# The following code illustrates a famous quote by George Bernard Shaw, using objects to represent people. 
# Fill in the blanks to make the code satisfy the behavior described in the quote.

# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw

class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
#Here, despite G.B. Shaw's quote, our characters have started with      
#different amounts of apples so we can better observe the results. 
#We're going to have Martin and Johanna exchange ALL their apples with #one another.
#Hint: how would you switch values of variables, 
#so that "you" and "me" will exchange ALL their apples with one another?
#Do you need a temporary variable to store one of the values?
#You may need more than one line of code to do that, which is OK.

# you = johanna
# me = martin

  applebag = you.apples
  you.apples = me.apples
  me.apples = applebag
  return you.apples, me.apples
    
def exchange_ideas(you, me):
    #"you" and "me" will share our ideas with one another.
    #What operations need to be performed, so that each object receives
    #the shared number of ideas?
    #Hint: how would you assign the total number of ideas to 
    #each idea attribute? Do you need a temporary variable to store 
    #the sum of ideas, or can you find another way? 
    #Use as many lines of code as you need here.
  you.ideas += me.ideas
  me.ideas = you.ideas
  return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))


# The City class has the following attributes: name, country (where the city is located), 
# elevation (measured in meters), and population (approximate, according to recent statistics). 
# 
# Fill in the blanks of the max_elevation_city function to return the name of the city and its country 
# (separated by a comma), when comparing the 3 defined instances for a specified minimal population. 
# For example, calling the function for a minimum population of 1 million: 
# max_elevation_city(1000000) should return "Sofia, Bulgaria".

# define a basic city class
class City:
	name = ""
	country = ""
	elevation = 0 
	population = 0

# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
# Initialize the variable that will hold 
# the information of the city with 
# the highest elevation 
	return_city = City()

	# Evaluate the 1st instance to meet the requirements:
	# does city #1 have at least min_population and
	# is its elevation the highest evaluated so far?
	if min_population <= city1.population:
		return_city = city1
		
	# Evaluate the 2nd instance to meet the requirements:
	# does city #2 have at least min_population and
	# is its elevation the highest evaluated so far?
	if min_population <= city2.population and  city2.elevation >= return_city.elevation:
		return_city = city2
		
	# Evaluate the 3rd instance to meet the requirements:
	# does city #3 have at least min_population and
	# is its elevation the highest evaluated so far?
	if min_population <= city3.population and  city3.elevation >= return_city.elevation:
		return_city = city3
		
	#Format the return string
	if return_city.name:
		return ("{}, {}".format(return_city.name, return_city.country))
	else:
		return ""

print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""

# We have two pieces of furniture: a brown wood table and a red leather couch. 
# Fill in the blanks following the creation of each Furniture class instance, so that 
# the describe_furniture function can format a sentence that describes these pieces as follows: 
# "This piece of furniture is made of {color} {material}"

class Furniture:
	color = ""
	material = ""

table = Furniture()
table.color = "brown"
table.material = "wood"

couch = Furniture()
couch.color = "red"
couch.material = "leather"

def describe_furniture(piece):
	return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))

print(describe_furniture(table)) 
# Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch)) 
# Should be "This piece of furniture is made of red leather"

class Piglet:
	name = "piglet"
	def speak(self):
		print ("oink! I'm {}! Oink!".format(self.name))
hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()
# Oink! I'm Hamlet! Oink!
petunia = Piglet()
petunia.name = "Petunia"
petunia.speak()
# Oink! I'm Petunia! Oink!

class Piglet:
	years = 0
	def pig_years(self):
		return self.years * 18

piggy = Piglet()
print(piggy.pig_years())
0
piggy.years = 2
print(piggy.pig_years())
36

# Create a Dog class with dog_years based on the Piglet class shown before 
# (one human year is about 7 dog years).
class Dog:
  years = 0
  def dog_years(self):
	  return self.years * 7
    
fido=Dog()
fido.years=3
print(fido.dog_years())

# Constructors and Other Special Methods
# The constructor of the class is the method that's called when you call the name of the class. It's always named init.

class Apple:
	def __init__(self,color,flavor):
	self.color = color
	self.flavor = flavor

jonagold = Apple("red", "sweet")
print(jonagold.color)
red

class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return ("hi, my name is {}".format(self.name))

# Create a new instance with a name of your choice
some_person = Person("Peteris")
# Call the greeting method
print(some_person.greeting())

class Apple:
	def __init__(self,color,flavor):
	self.color = color
	self.flavor = flavor
	def __str__(self):
		return "This apple is {} and its flavor is {}".format(self.color, self.flavor)


jonagold = Apple("red", "sweet")
print(jonagold.color)
red

# When we don't specify a way to print an object, Python uses the default 
# method that prints the position where the object is stored in the 
# computer's memory.

class Piglet:
	"""Represents a piglet that can say their name"""
	years = 0
	name  = ""
	def speak(self):
		print ("oink! I'm {}! Oink!".format(self.name))
	def pig_years(self):
	return self.years * 18
hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()

def to_seconds(hours,minutes,seconds)
  """Returns the amount of seconds in given hours, minuts, and seconds."""
  returns hours*3600+minutes*60+seconds 

help(to_seconds)

class Piglet:
	"""Represents a piglet that can say their name"""
	years = 0
	name  = ""
	def speak(self):
		"""Outputs a message including the name of the piglet."""
		print ("oink! I'm {}! Oink!".format(self.name))
	def pig_years(self):
		"""Converts the current age to equivalent pig years."""
	return self.years * 18
hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()

Defining classes and methods
class ClassName:
    def method_name(self, other_parameters):
        body_of_method

Classes and Instances
Classes define the behavior of all instances of a specific class.
Each variable of a specific class is an instance or object.
Objects can have attributes, which store information about the object.
You can make objects do work by calling their methods.
The first parameter of the methods (self) represents the current instance.
Methods are just like functions, but they can only be used through a class.
Special methods
Special methods start and end with __.
Special methods have specific names, like __init__ for the constructor or __str__ for the conversion to string.
Documenting classes, methods and functions
You can add documentation to classes, methods, and functions by using docstrings right after the definition. Like this:
class ClassName:
    """Documentation for the class."""
    def method_name(self, other_parameters):
        """Documentation for the method."""
        body_of_method
        
def function_name(parameters):
    """Documentation for the function."""
    body_of_function


####

class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current
        
    def up(self):
        """Makes the elevator go up one floor."""
        if self.current == self.top:
            self.current = self.top
        else:
            self.current += 1
            
    def down(self):
        """Makes the elevator go down one floor."""
        if self.current == self.bottom:
            self.current = self.bottom
        else:
            self.current -= 1
            
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        if floor <= self.top or floor >= self.bottom:
            self.current = floor
    def __str__(self):
        return "Current floor: {}".format(self.current)

elevator = Elevator(-1, 10, 0)
print(elevator.current)
# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current) # should be 9
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current) # should be 1

# Inheritance

class Fruit:
	def __init__(self, color, flavor):
		self.color = colorself.flavor = flavor

class Apple(Fruit):
	pass
class Grape(Fruit):
	pass
# Fruits is the paretn class and Apple & Grape are sibilings
# Instance of the Apple class

granny_smith = Apple("green", "tart")
carnelian = Grape("purple", "sweet")
print(granny_smith.flavor)
print(carnelian.color)

class Animal:
	sound = ""
	def __init__(self, name):
		self.name = name
	def speak(self):
		print("{sound} I'm {name}! {sound}".format(name=self.name, sound=self.sound))

class Piglet(Animal):
	sound = "Oink!"

hamlet = Piglet("Hamlet")
hamlet.speak()
Oink! ImportErrorm Hamlet! Oink!

class Cow(Animal):
	sound = "Moooo"

	milky = Cow("Milky White")
	milky.speak()
	Moooo I'm Milky White! Moooo

class Clothing:
  material = ""
  def __init__(self,name):
    self.name = name
  def checkmaterial(self):
	  print("This {} is made of {}".format(self.name,self.material))
			
class Shirt(Clothing):
  material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()

# Composition (Optional)

class Repository:
	def __init__(self):
		self.packages = {}
	def add_package(self, package):
		self.packages[package.name] = package
	def total_size(self):
		result = 0
		for package in self.packages.values():
			result += package.total_size #or package.size
		return result
# Your mission: Finish the "Stock_by_Material" method and iterate over 
# the amount of each item of a given material that is in stock. 
# When you’re finished, the script should add up to 10 cotton Polo shirts.

class Clothing:
  stock={ 'name': [],'material' :[], 'amount':[]}
  def __init__(self,name):
    material = ""
    self.name = name
  def add_item(self, name, material, amount):
    Clothing.stock['name'].append(self.name)
    Clothing.stock['material'].append(self.material)
    Clothing.stock['amount'].append(amount)
  def Stock_by_Material(self, material):
    count=0
    n=0
    for item in Clothing.stock['material']:
      if item == material:
        count += Clothing.stock['amount'][n]
        n+=1
    return count

class shirt(Clothing):
  material="Cotton"
class pants(Clothing):
  material="Cotton"
  
polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)

class Zoo:
    def __init__(self):
        self.current_animals = {}
    
    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category
    
    def total_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            if animal == category:
                result += 1
        return result

zoo = Zoo()

turtle = Turtle("Turtle") #create an instance of the Turtle class
snake = Snake("Snake") #create an instance of the Snake class

zoo.add_animal(turtle)
zoo.add_animal(snake)

print(zoo.total_of_category("reptile")) #how many zoo animal types in the reptile category


# Python Modules (Optional)
import random
random.randint(1, 10)
1
random.randint(1, 10)
4
random.randint(1, 10)
6

import datetime
now = datetime.datetime.now()
type(now)
print(now)
print (now + datetime.timedelta(days=28))


#Begin Portion 1#
import random

class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        # Add the connection to the dictionary with the calculated load
        self.connection_id = connection_id
        self.connections[connection_id] = connection_load
    
    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        # Add up the load for each of the connections
        for conload in server.connections.values():
            print(conload)
            total += conload
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())
    
#End Portion 1#
server = Server()
server.add_connection("192.168.1.1")

print(server.load())