arr = [3, 7, 5, 1, 2, 4, 9, 8, 6]

def selSort(lst1):
    for i in range(len(lst1)):
        n = i
        for j in range(i+1, len(lst1)):
            if lst1[j] < lst1[n]:
                n = j
        lst1.insert(i, lst1.pop(n))
    return lst1

print(selSort(arr))

#*****************************SOLUTION*************************************

my_arr = [-64, 25, -12, 22, 11] 

for i in range(len(my_arr)): 
    min_idx = i 
    for j in range(i+1, len(my_arr)): 
        if my_arr[min_idx] > my_arr[j]: 
            min_idx = j
    temp = my_arr[i]
    my_arr[i] = my_arr[min_idx]
    my_arr[min_idx] = temp

print(my_arr)    