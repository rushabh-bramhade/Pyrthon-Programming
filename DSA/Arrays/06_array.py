# Methods of arrays 

arr = [2,3,4,5,3,4,5,6,6,64,5,3,5,3,5,3,4,5,24,6]

arr.append(1)
arr.append(2)
arr.insert(1,1)
arr.insert(0,1)
arr.pop(1)
arr.pop(0)
arr.remove(1)
arr.remove(1)



print(arr[::-1])

for i in range(len(arr)):
    print(arr[i],end=" ")


if 2 in arr:
    print(f"found { arr.count(3)}")
else:
    print("not found")