# This program finds the smallest number in a list.

smallest_so_far = None
for i in [32, 6, 12, 633, 54, 4] :
    if smallest_so_far is None :
        smallest_so_far = i
    elif i < smallest_so_far :
        smallest_so_far = i
    print(i, smallest_so_far)
print('The smallest so far is', smallest_so_far)
