# 1.Write a Python program that takes an integer as input and checks whether the number is even or odd.
# Input: 7
# Output: The number 7 is odd.

str1 = "Even and Odd Number"
print(str1.center(50,"="))

number = int(input("Enter a number: "))
print ("The number is: ", number)

if number > 0:
    print("The number is positive")
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
elif number < 0:
    print("The number is negative")
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("The number is zero")