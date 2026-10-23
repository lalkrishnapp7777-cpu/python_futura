# a = [1,2,3,4,5,6]
# n = 3
# b = len(a) / n
# for i in range(0, len(a), b):

arr = [1,2,2,3,4]
for i in arr[:]:
 if i == 2:
   arr.remove(i)
print(arr)