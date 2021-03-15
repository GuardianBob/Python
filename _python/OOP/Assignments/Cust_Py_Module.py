# Your assignment is to implement the 4 methods shown using callbacks. 
# You will have to modify the 4 methods to take in a list and a callback. 
# A callback is simply a function that is passed as an argument, 
# to be executed by the function to which it is being passed. 
# Just as we are able to pass numbers, lists, strings, etc. when making a function call, 
# we can also pass functions! That means we do not invoke the function right away, 
# but rather pass the function by using the name only (i.e. not including the ()). 
# In the examples at the bottom, we are specifically passing lambda functions:

class Underscore:
    def map(self, iterable, callback):
        for x in range(len(iterable)):
            iterable[x] = callback(iterable[x])
        return iterable
    
    def find(self, iterable, callback):
        for val in iterable:
            if callback(val):
                return val
    
    def filter(self, iterable, callback):
        new_arr = []
        for val in iterable:
            if callback(val):
                new_arr.append(val)
        return new_arr
    
    def reject(self, iterable, callback):
        new_arr = []
        for val in iterable:
            if not callback(val):
                new_arr.append(val)
        return new_arr
        

_ = Underscore()
_.map([1,2,3], lambda x: x*2) # should return [2,4,6]
found = _.find([1,2,3,4,5,6], lambda x: x > 4) # should return the first value that is greater than 4
_.filter([1,2,3,4,5,6], lambda x: x%2==0) # should return [2,4,6]
reject = _.reject([1,2,3,4,5,6], lambda x: x%2==0) # should return [1,3,5]