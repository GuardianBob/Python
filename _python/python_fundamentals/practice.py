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

# 

import json, requests

xUrl = 'https://pokeapi.co/api/v2/pokemon/5/'
# y = json.loads(xUrl)
# for i in y["moves"]: #["abilities"]:
#     print(i["move"]["name"]) #["ability"]["name"])

pUrl = requests.get(xUrl)
cvt = pUrl.json()
print(cvt['name'])
# y = json.loads(pUrl.read())
# print(y['name']) #["ability"]["name"])

users.objects.create(first_name)