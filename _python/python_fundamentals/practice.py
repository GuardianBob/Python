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

# import json, requests

# xUrl = 'https://pokeapi.co/api/v2/pokemon/5/'
# # y = json.loads(xUrl)
# # for i in y["moves"]: #["abilities"]:
# #     print(i["move"]["name"]) #["ability"]["name"])

# pUrl = requests.get(xUrl)
# cvt = pUrl.json()
# print(cvt['name'])
# # y = json.loads(pUrl.read())
# # print(y['name']) #["ability"]["name"])

# users.objects.create(first_name)

# import bcrypt
# # pw = b"test"
# # .encode() just adds a "b" in front of the password in apostrphies: b'passwprd'.
# hash1 = bcrypt.hashpw('test'.encode(), bcrypt.gensalt())
# print(hash1)

# if bcrypt.checkpw('test'.encode(), hash1):
#     print("Matched")
# else:
#     print("nope")

# import datetime
# date1 = datetime.date.today()
# minDate = datetime.date(date1.year + 13, date1.month, date1.day)
# print(minDate)
# if date1 > minDate:
#     print("greater")
# else:
#     print("Less")

# string = "First Second Last"
# fName = string.split(" ", 1)[0]
# lName = string.split(" ", 1)[1]
# print(fName, " : ", lName)

# import json
# # Python's built-in module for opening and reading URLs
# from urllib.request import urlopen

# while True:
#     api = "https://www.googleapis.com/books/v1/volumes?q=intitle:"
#     in1 = input("Enter title: ").strip()
#     title = in1.replace(" ", "%20")
#     key1 = "&key=AIzaSyC0QCgMWSfhNnDAMQ6S6--fNE1J2Ul5LEU"

#     resp = urlopen(api + title + "")
#     # parse JSON into Python as a dictionary
#     book_data = json.load(resp)

#     # create additional variables for easy querying
#     volume_info = book_data["items"][0]["volumeInfo"]
#     author = volume_info["authors"]
#     # practice with conditional expressions!
#     prettify_author = author if len(author) > 1 else author[0]

#     # display title, author, page count, publication date
#     # fstrings require Python 3.6 or higher
#     # \n adds a new line for easier reading
#     print(f"\nTitle: {volume_info['title']}")
#     print(f"Author: {prettify_author}")
#     print(f"Page Count: {volume_info['pageCount']}")
#     print(f"Publication Date: {volume_info['publishedDate']}")
#     print("\n***\n")

#     # ask user if they would like to enter another isbn
#     user_update = input("Would you like to enter another ISBN? y or n ").lower().strip()

#     if user_update != "y":
#         print("May the Zen of Python be with you. Have a nice day!")
#         break # as the name suggests, the break statement breaks out of the while loop


# import pytz
# for tz in pytz.all_timezones:
#     print(tz)

# def local_time_update(infos):
#     now = datetime.datetime.now()
#     local_now = now.astimezone()
#     local_tz = local_now.tzinfo
#     for info in infos:
#         time1 = info.created_at         
#         utc = time1.replace(tzinfo=pytz.UTC) 
#         localT = utc.astimezone(local_tz)
#         info.created_at = localT
#         # print(localT)
#     return infos


# def local_time_single(time1):
#     now = datetime.datetime.now()
#     local_now = now.astimezone()
#     local_tz = local_now.tzinfo
#     utc = time1.replace(tzinfo=pytz.UTC)
#     localT = utc.astimezone(local_tz)
#     # # info.created_at = localT
#     # # localT = timezone.localdate(time1)    
#     print(time1, " : ", localT)
#     return