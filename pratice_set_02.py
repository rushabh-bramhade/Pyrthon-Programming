# Write a program to store the 7 fruit in the list entered by user

print("Enter the 7 fruits into the list")

fruit = []

f1 = input("Enter the fruit name :")
fruit.append(f1)

f2 = input("Enter the  fruit name :")
fruit.append(f2)

f3 = input("Enter the fruit name :")
fruit.append(f3)

f4 = input("Enter the  fruit name :")
fruit.append(f4)

f5 = input("Enter the  fruit name :")
fruit.append(f5)

f6 = input("Enter the  fruit name :")
fruit.append(f6)

f7 = input("Enter the fruit name :")
fruit.append(f7)

print(fruit)


# Write a program to accept marks of 6 student and display them in a stored manner


marks = []

s1 = float(input("Enter the first student marks : "))
marks.append(s1)

s2 = float(input("Enter the second student marks : "))
marks.append(s2)

s3 = float(input("Enter the thrid student marks : "))
marks.append(s3)

s4 = float(input("Enter the fourth student marks : "))
marks.append(s4)

s5 = float(input("Enter the fifty student marks : "))
marks.append(s5)

s6 = float(input("Enter the sixty student marks : "))
marks.append(s6)

marks.sort()

print(marks)


# Write a program to count the number of zero in the following tuple

a = (7,0,8,0,0,9)

print(a.count(0))