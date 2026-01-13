#number accept by the user and printing the number by using array
import array

n = int(input("How many number you want to store in array :"))
number = array.array('i',[0] * n)

for i in range(n):
    number[i] = int(input(f"Enter the number {i+1} :"))

for i in range(len(number)):
    print(number[i])


# using the numpy module 
import numpy as np


n = int(input("How many number you want to store :"))
number = np.zeros(n,dtype = int)

for i in range(n):
    number[i] = int(input(f"Enter the number {i+1} :"))

for i in range(len(number)):
    print(number[i],end=" ")