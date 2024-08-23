# Define a function called greet_user that:
# Takes one argument, name.
# Prints a greeting message that includes the name.

str1 = " Greating "
print(str1.center(50,"="))
def greet_user(name):
    print("Name:- " + name + ".")

greet_user("Alice")
greet_user("Bob")
greet_user("Charlie")

# Modify the greet_user function:
# Add a second optional argument, greeting, with a default value of "Hello".
# The function should print the greeting followed by the name.

str1 = " Greating_Modi "
print(str1.center(50,"="))
def greet_user(name, greeting="Hello",):
    print(greeting, name, "!")

greet_user("Alice")
greet_user("Bob")
greet_user("Charlie")
