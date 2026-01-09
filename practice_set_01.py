# 1. write a python program to add two numbers

num1 = 5
num2 = 15

print(f"Adding the num1 : {num1} and num2 : {num2} are ", num1 + num2)

# write a python program to find the remainder which a number is divided by z

z = 3

print(z % num1)

# checking the type of variable assigned using input () function 

var = input("Enter the variable value as string :") # Here input() function always convert's the values in the string as 'str'

print("The type of the variable enter was :", type(var)) 

# Use comparison operator to find out whether a given variable is greater than 'b' or not. Take a = 34 and b = 80

a = 34
b = 80

print("The varriable 'b' is greater than a :", b > a)

# Write a python program to find the average values of two numbers entered by the user's

val_1 = int(input("Enter the first value as interger :"))
val_2 = int(input("Enter the second value as interger :"))

result = val_1 + val_2 / 2

print("The average values is :", result)


# Write a pyton program to find the square values of number which entered by the user's

square_val = int(input("Enter the values for square :"))

square = square_val ** 2 # ** is the power operator used to find the square values 

print("The result of this values :", square)

#count the length 

string_len = "Hello world"

print(len(string_len))