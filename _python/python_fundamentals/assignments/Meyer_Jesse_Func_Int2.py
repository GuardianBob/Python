# 1. Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}    
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

def chngListVal(list1, oldVal, newVal):
    for x in list1:
        for val in range(len(x)):
            if x[val] == oldVal:
                x[val] = newVal
    return list1

def chngKeyLstVal(list1, oldVal, newVal):
    for x in list1:
        for val in x:
            if x.get(val) == oldVal:
                x.update({val: newVal})
    return list1

def chngDictVal(dict1, oldVal, newVal):
    for val in dict1.values():
        for v in range(len(val)):
            if val[v] == oldVal:
                val[v] = newVal
    return dict1

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
chngListVal(x, 10, 15)
print(x)
# Change the last_name of the first student from 'Jordan' to 'Bryant'
chngKeyLstVal(students, "Jordan", "Bryant")
print(students)
# In the sports_directory, change 'Messi' to 'Andres'
chngDictVal(sports_directory, 'Messi', 'Andres')
print(sports_directory)
# Change the value 20 in z to 30
chngKeyLstVal(z, 20, 30)
print(z)

# 2. Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, 
# the function loops through each dictionary in the list and prints each key and the 
# associated value. For example, given the following list:

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary(lst1): 
    for dict1 in lst1:
        itm = []
        for key, val in dict1.items():
            itm.append(key + " - " + val)
        print(itm)

iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# 3. Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, 
# given a list of dictionaries and a key name, the function prints 
# the value stored in that key for each dictionary. 
def iterateDictionary2(key_name, some_list):
    for dict1 in some_list:
        for key, val in dict1.items():
            if key == key_name:
                print(val)

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)
# For example, iterateDictionary2('first_name', students) should output:
# Michael
# John
# Mark
# KB

# 4. Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values 
# are all lists, prints the name of each key along with the size of its list, 
# and then prints the associated values within each key's list.
def printInfo(dict1):
    for key, val in dict1.items():
        print(len(val), key)
        for i in val:
            print(i)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)

#--------------------------------------------
# --------------SOLUTIONS--------------------
#--------------------------------------------


# 1. Update Values in Dictionaries and Lists
x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

# Change the value 10 in x to 15. Once you're done, x should now be[[5, 2, 3], [15, 8, 9]].
x[1][0] = 15
print(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students)

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

# Change the value 20 in z to 30
z[0]['y'] = 30
print(z)

# 2. Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
# there are some power moves here
# find all the logic you understand, look up what you don't
# ask if you don't quite get it
def iterate_dictionary(some_list):
    for curr_dict in some_list:
        display_str = ''
        for curr_key in curr_dict.keys():
            display_str += f"{curr_key} - {curr_dict[curr_key]}, "
        # remove comma and extra space from display_str
            display_str = display_str[:len(display_str) - 2]
        print(display_str)

iterate_dictionary(students)

# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:

# Michael
# John
# Mark
# KB
# And iterateDictionary2('last_name', students) should output:

# Jordan
# Rosales
# Guillen
# Tonel

def iterate_dictionary2(key, some_list):
    for curr_dict in some_list:
        print(curr_dict[key])

iterate_dictionary2('first_name', students)
iterate_dictionary2('last_name', students)

# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

def print_info(some_dict):
    for key in some_dict.keys():
        print(f"{len(some_dict[key])} {key.upper()}")
        for item in some_dict[key]:
            print(item)
            # this prints a new line
        print('\n')

print_info(dojo)