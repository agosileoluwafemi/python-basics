# This program finds the largest number in a list.

largest_so_far = None
for i in [32, 6, 12, 633, 54, 4] :
    if largest_so_far is None :
        largest_so_far = i
    elif i > largest_so_far :
        largest_so_far = i
    print(i, largest_so_far)
print('The largest so far is', largest_so_far)
