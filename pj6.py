# Create a function sum_numbers that:
# Takes two arguments, a and b.
# Returns the sum of a and b.


str1 = " Sum_Number "
print(str1.center(50,"="))

a = (input(" Enter 1st number:"))
b = (input(" Enter 2nd number:"))

def sum_numbers(a,b):
    return a + b
print("The total of", a, "and", b, "=", sum_numbers(a,b))