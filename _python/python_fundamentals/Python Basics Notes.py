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

# Simple swap method:
arr = [1,3,5,7]
arr[0], arr[1] = arr[1], arr[0]

# Bubble Swap
# The following will loop through an array/list and sort from lowest to highest
def bubbleSwap(lst1):
    n = len(lst1)
    for i in range(n-1):        #This will run through the full list once (from 0 to 5)
        for j in range(n-i-1):      #This starts as 0 to 5 since i is at 0 for first run
            # The first iteration will carry the largest number to the end.
            # The second iteration only goes to the second to last number since the last is already the largest.
            # Each iteration carries the largest number to the last number in the range
            # Range 1: 0 - 5, 2: 0 - 4, 3: 0 - 3, etc.
            if lst1[j] > lst1[j+1]:
                lst1[j], lst1[j+1] = lst1[j+1], lst1[j]

arr = [2, 6, 1, 5, 3, 4]
arr2 = bubbleSwap(arr)
print(arr)

# *******************Ternary Operator  *******************
# A ternary operator, or conditional expression, is an operator that takes 3 arguments. 
# Most simply, they are a one line if-else statement. In many languages, 
# we see this same functionality with the symbols ? and :. In Python, the syntax is as follows:
# <result_if_true> if <condition> else <result_if_false>
# Example:

# traditional
if stacks >= 3:
    print('Coding Dojo')
else:
    print('You are not Coding Dojo!')
# *********ternary**********
print('Coding Dojo' if stacks >= 3 else 'You are not Coding Dojo!')

#***********************    Lambdas *******************
# In Python, anonymous functions are created with the lambda keyword. These functions are used for various purposes:
# they are handy in situations where we only need to use the function once
# they are lightweight when we need to break down complex tasks into small, specific tasks
# they are convenient as arguments to functions that require functions as parameters
# Example:  defined:
def square(num):
    x = num ** 2
    return x
# Lambda that does the same as above:
lambda num: num ** 2
# Lambdas can take multiple arguments as well.  Example:
lambda num1, num2: num1+num2
# This takes two arguments and returns the sum of those args
# Lambdas can be elements in a list as well

# create a new list, with a lambda as an element
my_list = ['test_string', 99, lambda x : x ** 2]
# access the value in the list
print(my_list[2]) # will print a lambda object stored in memory
# invoke the lambda function, passing in 5 as the argument
my_list[2](5)

# define a function that takes one input that is a function
def invoker(callback):
    # invoke the input pass the argument 2
    print(callback(2))
invoker(lambda x: 2 * x)
invoker(lambda y: 5 + y)

# !!!!!!! Can be stored as variables
add10 = lambda x: x + 10 # store lambda expression in a variable
add10(2)  # returns 12
add10(98) # returns 108

# ********************* map() function ***************
# Map basically maps a list to a function
# Python program to demonstrate working 
# of map. 

# Return double of n 
def addition(n): 
	return n + n 

# We double all numbers using map() 
numbers = (1, 2, 3, 4)   
result = map(addition, numbers)   # Maps the "numbers" list to the "addition" function 
print(list(result)) 
# result = addition(numbers)  <--------THis does not work here because the function can only accept a single argument

# ***********************   Slicing     *********************
# Allows for getting subset of values from a sequence
# We indicate the starting index on the left and the ending index (exclusive) on the right. If we don't indicate a value on the left, it will start at index 0; if the value on the right is not specified, it will assume the length of the sequence.
my_list = [99,4,2,5,-3]
my_tuple = (99,4,2,5,-3)
my_str = "sequoia"
print(my_list[:])
# output: [99,4,2,5,-3]
print(my_tuple[1:])
# output: (4,2,5,-3)
print(my_str[:3])
# output: "seq"
print(my_tuple[2:4])
# output: (2,5)
print(my_list, my_tuple, my_str)
# output: [99,4,2,5,-3] (99,4,2,5,-3) 'sequoia' -- note the original values have not changed


