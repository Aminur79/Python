# 4.Write a Python program that counts the number of vowels (a, e, i, o, u) in a given string.
# Input: Hello World
# Output: The number of vowels in "Hello World" is 3.

s = input("Enter a string: ")
vowel_count = 0
for char in s:
    if char.lower() in 'aeiou':
        vowel_count += 1
print(f"The number of vowels in \"{s}\" is {vowel_count}.")