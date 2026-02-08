# This program finds the average of numbers in a list.

count = 0
sum = 0
for i in [32, 6, 12, 633, 54, 4] :
    count = count + 1
    sum = sum + i
avg = sum / count
print(avg)
