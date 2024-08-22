# 3.Write a Python program that takes three numbers as input from the user and prints the largest one.
# Input: 12, 25, 7
# Output: The largest number is 25.

str1 = "Larger Number Selected"
print(str1.center(50,"="))

a = int(input ("Enter your 1st number: "))
b = int(input ("Enter your 2nd number: "))
c = int(input ("Enter your 3rd number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and a >= c:
    largest = b
else:
    largest = c

print(50*"=")
print ("The largest number is:", largest)
print(50*"=")