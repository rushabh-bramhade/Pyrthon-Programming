
arr = [1,23,4,5,6,7,8,4]

prefix = [0] * len(arr)
prefix[0] = arr[0]
# if not arr:
#   return arr
for i in range(1,len(arr)):
    prefix[i] = prefix[i - 1] + arr[i]

print(prefix)



"""
if not arr:
    return arr
= Safety check for empty arrays

Situation	Use it?
Accessing arr[0]	✅ Yes
Using prefix sum	✅ Yes

7. Simple Real-Life Analogy

Before opening the first page of a book, you check:

“Does the book have pages?”

"""