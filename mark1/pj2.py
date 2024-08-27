# 2.Write a Python program that generates the multiplication table of a number provided by the user.


str1 = "Multiplication"
print(str1.center(50,"="))

number = int(input("Enter a number: "))
print ("The number is: ", number)

print(50*"=")

print("Multiplication table of", number)
for i in range(1, 13):
    print(i, "x", number, "=", i * number)
    
print(50*"=")