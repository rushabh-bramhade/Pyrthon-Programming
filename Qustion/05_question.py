# Problem:
# Take two numbers and print the larger one.

user_num1 = int(input("Enter the first number :"))
user_num2 = int(input("Enter the second number :"))

if user_num2 < user_num1:
    print(f"{user_num1} : is greater than  {user_num2} : is lesser ")
elif user_num2 > user_num1:
    print(f"{user_num2} : is greater than  {user_num1} : is lesser ")
elif user_num2 == user_num1:
    print(f"{user_num2} : is equal numbers as {user_num1}")
print("code executed successfully...")




