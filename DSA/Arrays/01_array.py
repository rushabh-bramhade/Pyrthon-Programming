from array import array 


user_input = int(input(f"Enter how many numbers you want to store in array :"))
arr = array('i',[])

for i in range(user_input):
    num = int(input(f"Enter the number {i + 1} :"))
    arr.append(num)
       
    
print(arr)
