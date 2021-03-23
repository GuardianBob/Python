# def a():
#     print(1)
#     x = b()
#     print(x)
#     return 10
# def b():
#     print(3)
#     return 5
# y = a()
# print(y)

# # Simple Swap:
# arr = [5, 4, 3, 2]
# arr[0], arr[1], arr[2], arr[3] = arr[3], arr[2], arr[1], arr[0]
# print(arr)

# def bubbleSwap(lst1):
#     n = len(lst1)
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if lst1[j] > lst1[j+1]:
#                 lst1[j], lst1[j+1] = lst1[j+1], lst1[j]

# arr = [2, 6, 1, 5, 3, 4]
# arr2 = bubbleSwap(arr)
# print(arr2)

# def minSort(lst1):
#     arr1 = []
#     while len(lst1) > 0:
#         n = lst1.index(min(lst1))
#         arr1.append(lst1[n])
#         lst1.remove(lst1[n])
#     return arr1

# arr = [2, 6, 1, 5, 3, 4]
# print(minSort(arr))

# def invoker(callback):
#     # invoke the input pass the argument 2
#     print(callback(2))
# invoker(lambda x: 2 * x)
# invoker(lambda y: 5 + y)

# def addition(n): 
# 	return n + n 

# # We double all numbers using map() 
# numbers = (1, 2, 3, 4)   
# result = map(addition, numbers)   # Maps the "numbers" list to the "addition" function 
# print(list(result)) 

# print(list(range(0, 100, 10)))

class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):

        def add_to_front(self, val):
            new_node = SList(val)


class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new.node.next = current_head
        self.head = new_node
        return self

    
    def print_values(self):
        runner = self.head
        while (runner != None):
            print (runner.value)
            runner = runner.next
        return self



    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self
            
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
            runner.next = new_node
        return self


my_list = SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()
