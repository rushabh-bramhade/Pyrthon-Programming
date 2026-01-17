

def marge_short(arr):

    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left  = arr[:mid]
    right = arr[mid:]
    left = marge_short(left)
    right = marge_short(right)
    return marge_arr(left,right)
    
def marge_arr(left,right):
    i , j = 0 , 0
    n , m = len(left) , len(right)
    result = []

    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
   
    return result

arr = [3,1,6,2,4,8,7]
output = marge_short(arr)
print(output)

