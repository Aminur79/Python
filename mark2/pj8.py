# Write a loop that:
# Prints numbers from 1 to 10.
# Stops the loop if the number is 7 (use the break statement).


str1 = " loop_break "
print(str1.center(50,"="))

for i in range(1,10):
    if i == 7:
        break
    print(i)

# Write a loop that:
# Prints numbers from 1 to 10.
# Skips the numbers that are multiples of 3 (use the continue statement).


str1 = " continue_numbers "
print(str1.center(50,"="))

for i in range(1,11):
    if i % 3 == 0:
        continue
    print(i)