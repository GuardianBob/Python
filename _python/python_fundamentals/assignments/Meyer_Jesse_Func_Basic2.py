# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, 
# from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]

def countdown(num):
    lst = []
    for x in range(num, -1, -1):         
        lst.append(x)
    return lst

lst1 = countdown(5)
print(lst1)
#   SOLUTION is same

# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2
def prntRtn(lst):
    print(lst[0])
    return lst[1]

lstNum = [1, 2]
x = prntRtn(lstNum)
print(x)

# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
def fstPLngth(lst):
    return lst[0] + len(lst)

y = [5,4,3,2,1]
print(fstPLngth(y))

# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values 
# from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. 
# If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False
def grtrLst(lst):
    if len(lst) < 2:
        return False
    else:
        lst2 = []
        for x in lst:
            if x > lst[1]:
                lst2.append(x)
        print(len(lst2))
        return lst2

nLst = [5, 3, 1, 7, 2]
print(grtrLst(nLst))

# This Length, That Value - Write a function that accepts two integers as parameters: size and value. 
# The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]
def lenVal(l, v):
    lst = []
    for x in range(l):
        lst.append(v)
    return lst

print(lenVal(4, 7))