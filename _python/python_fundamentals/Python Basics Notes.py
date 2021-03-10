name = "Zen"
print("my name is", name)  #Print inserts a space between comma-separated elements.
print("my name is " + name)   # "+" concatenates elements.

# F-Strings
#To construct an f-string, place an f right before the opening quotation. Then within the string, place any variables within curly brackets.
first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")  #"f" allows for easy inclusion and automatically converts integers to strings

#string.format():
#use this to replace "{}" brackets with a list of strings included at the end in the .format() parenthesis
#This method always reads from left to right:
first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.

# %-formatting
#the % symbol is used to indicate a placeholder, a %s for a string and %d for a number.
# After the string, a single % separates the string to be interpolated from the values to be inserted into the string, like so:
hw = "Hello %s" % "world" 	# with literal values
py = "I love Python %d" % 3 
print(hw, py)
# output: Hello world I love Python 3
name = "Zen"
age = 27
print("My name is %s and I'm %d" % (name, age))		# or with variables
# output: My name is Zen and I'm 27


#Code blocks (if, for, etc) require indentation (4 spaces) rather than brackets:
x = 10
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")
#without the "print" function being indented, the program would error out.

#***Pass - If we start a code block, there must be at least one line of indented code immediately following. 
# If we try to run a file with a hanging code block, we'll get a syntax error. 
# Luckily, Python has provided us with the pass statement for situations where we know we need the block statement, 
# but we aren't sure what to put in it yet.
# the pass statement is null operation
class EmptyClass:
    pass

#Tuples - A type of data that is immutable (can't be modified after its creation) and can hold a group of values. 
# Tuples can contain mixed data types.
dog = ('Bruce', 'cocker spaniel', 19, False)
print(dog[0])		# output: Bruce
dog[1] = 'dachshund'	# ERROR: cannot be modified ('tuple' object does not support item assignment)


#Lists - A type of data that is mutable and can hold a group of values. Usually meant to store a collection of related data.
empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) 	# output: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)	# output: ['Francis', 'Oliver']


#Dictionaries - A group of key-value pairs. Dictionary elements are indexed by unique keys which are used to access values.
empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'	# updates if the key exists
new_person['hobbies'] = ['climbing', 'coding']	# adds a key-value pair if the key doesn't exist
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight')	# removes the specified key and returns the value
print(w)		# output: 160.2
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}        


#If we're ever unsure of a value or variable's data type, we can use the type function to find out. For example:
print(type(2.63))		# output: <class 'float'>
print(type(new_person))		# output: <class 'dict'>


#For data types that have a length attribute (eg. lists, dictionaries, tuples, strings), we can use the len function to get the length:
print(len(new_person))		# output: 4 (the number of key-value pairs)
print(len('Coding Dojo'))	# output: 11


#Python doesn't know how to add a string and a number, but it can add two strings together, 
# so if we can cast the number as a string, then we will be able to "add" the two values together, like so:
print("Hello" + 42)			# output: TypeError
print("Hello" + str(42))		# output: Hello 42


total = 35
user_val = "26"
total = total + user_val		# output: TypeError
total = total + int(user_val)		# total will be 61

# if, elif, else
# always returns the first true conditional
x = 55
if x > 10:
    print("bigger than 10")
elif x > 50:
    print("bigger than 50")
else:
    print("smaller than 10")
# even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'

#Loops
#for variable in range(start, stop, change by)
for x in range(0, 10, 1):
    pass
for x in range(0, 10):	# increment of +1 is implied
    pass
for x in range(10):	# increment of +1 and start at 0 is implied
    pass

#Example 1:
for x in range(0, 10, 2):
    print(x)
# output: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
# output: 5, 2

#Example 2:
my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz
    
# OR 
    
for v in my_list:  #This will iterate through the entire list
    print(v)
# output: abc, 123, xyz

#Dictionaries iterate through the keys or the key values based on how it's specified:
#Iterate through keys:
my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k)
# output: name, language

#Iterate through values:
my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(my_dict[k])
# output: Noelle, Python

# another way to iterate through the keys
capitals = {"Texas": "Austin", "Kansas": "Topeka", "Massachusettes": "Boston" }
for key in capitals.keys():
    print(key)
#to iterate through the values
for val in capitals.values():
    print(val)
#to iterate through both keys and values
for key, val in capitals.items():
    print(key, " = ", val)


# While Loops
for count in range(0,5):
    print("looping - ", count)
#can also be written
count = 0
while count < 5:
    print("looping - ", count)
    count += 1

#basic syntax for While loop:
#while <expression>:  do something, including progress towards making the expression False. Otherwise we'll never get out of here!

#Breaks
#When loops are nested, a break will only exit from the innermost loop.
for val in "string":
    if val == "i":
        break
    print(val)
# output: s, t, r

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
    print("Final else statement")
# output: 3, 2, 1


#Continue  - jumps back to the beginning of the loop, skipping the current iteration
for val in "string":
    if val == "i":
        continue
    print(val)
# output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i


#Functions
#The def keyword signifies the declaration of a function.