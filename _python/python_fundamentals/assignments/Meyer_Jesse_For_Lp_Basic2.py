# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def bgSz(lst):
    for x in range(len(lst)):
        if lst[x] > 0:
            lst[x] = "big"
    return lst

print(bgSz([-1, 3, 5, -5]))

#   SOLUTION
def biggie_size(lst):
    # use range because we need to replace values in specific indices
    for i in range(len(lst)):
        if lst[i] > 0:
            lst[i] = "big"
    return lst

print(biggie_size([-1, 3, 5, -5]))

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. 
# (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def cntPos(lst):
    y = 0
    for x in range(len(lst)):
        if lst[x] > 0:
            y += 1
    lst[len(lst)-1] = y
    return lst

print(cntPos([-1,1,1,1]))

#   SOLUTION
def count_positives(lst):
    count = 0
    for val in lst:
        if val > 0:
            count += 1
    lst[len(lst) - 1] = count
    return lst

print(count_positives([-1, 1, 1, 1]))
print(count_positives([1, 6, -4, -2, -7, -2]))

# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def sumTot(lst):
    y = 0
    for x in lst:
        y += x
    return y

print(sumTot([6,3,-2]))

#   SOLUTION SAME


# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5
def avgLst(lst):
    y = 0
    for x in lst:
        y += x
    y = y / len(lst)
    return y

print(avgLst([1,2,3,4]))

#   SOLUTION
def average(lst):
    total = 0
    for val in lst:
        total += val
    # if we want a non-integer we must convert at least one number to a float
    # I chose to convert both for safe measure
    # typically, we want to be hyper cautious and allow python to do as little
    # inference as possible
    return float(total) / float(len(lst))

print(average([1 ,2 ,3 , 4]))

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
def lng(lst):
    return len(lst)

print(lng([37,2,1,-9]))

#   SOLUTION


# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
def minm(lst):
    if len(lst) == 0:
        return False
    else:
        return min(lst)

print(minm([37,2,1,-9]))

#   SOLUTION


# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
def mxm(lst):
    if len(lst) == 0:
        return False
    else:
        return max(lst)

print(mxm([37,2,1,-9]))

#   SOLUTION


# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultAn(lst):    
    dict1 = {
        "sumTotal": sum(lst),
        "average": sum(lst) / len(lst),
        "minimum": min(lst),
        "maximum": max(lst),
        "length": len(lst)
    }
    return dict1

print(ultAn([37,2,1,-9]))

#   SOLUTION
def ultimate_analysis(lst):
    # handle
    result = {
        'sum_total': None,
        'maximum': None,
        'minimum': None,
        'average': None,
        'length': 0
    }
    if len(lst) == 0:
        return result
    else:
        result['sum_total'] = 0
        result['maximum'] = lst[0]
        result['minimum'] = lst[0]
    
    for val in lst:
        if val > result['maximum']:
            result['maximum'] = val
        elif val < result['minimum']:
            result['minimum'] = val

        result['sum_total'] += val
        result['length'] += 1
    result['average'] = result['sum_total'] / len(lst)

    return result

print(ultimate_analysis([37, 2, 1, -9]))
print(ultimate_analysis([]))


# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. 
# (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def rev_lst(lst):
    i = 0
    j = len(lst) -1
    while i < j:
        tmp = lst[i]
        lst[i] = lst[j]
        lst[j] = tmp
        i += 1
        j -= 1
    return lst

print (rev_lst([37,2,1,-9]))

# OR

def rev_lst2(lst):
    return lst[::-1]

print (rev_lst2([37,2,1,-9]))

#  OR

def rev_lst3(lst):
    lst.reverse()
    return lst

print (rev_lst3([37,2,1,-9]))


#  SOLUTION

def reverse_list(lst):
    half_len = int(len(lst) / 2)
    for i in range(half_len):
        # this is a neat way to do a python swap, a temp is equally valid
        lst[i] , lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]
    return lst

# some robust test cases
print(reverse_list([37, 2, 1, -9]))
print(reverse_list([37, 2, 1, -9, 5]))
print(reverse_list([]))
print(reverse_list([1]))
print(reverse_list([1, 2]))