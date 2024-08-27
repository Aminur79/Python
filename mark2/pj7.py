# Work with the following list: fruits = ["apple", "banana", "cherry", "date"].
# Perform the following operations:
# Add "elderberry" to the end of the list.
# Remove "banana" from the list.
# Insert "blueberry" at the second position in the list.
# Sort the list in alphabetical order.


str1 = " Fruits "
fruits = ["apple", "banana", "cherry", "date"]
print(str1.center(50,"="))


fruits.append("elderberry")
print("1", fruits)

fruits.remove("banana")
print("2", fruits)

fruits.insert(1, "blueberry")
print("3", fruits)

fruits.sort()
print("sorted list",fruits)