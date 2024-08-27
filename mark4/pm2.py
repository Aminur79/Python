#try 1
# import os

# c = 0

# def increment_counter():
#     global c
#     c += 1
#     print(f"Global counter:{c}")

# def reset_counter():
#     global c
#     c = 0
#     print(f"Global counter:{c}")

# increment_counter()
# increment_counter()
# increment_counter()

# reset_counter()
# print(f"Global reset:{c}")


#try 2
# cwd = os.getcwd()
# print(f"Current dir:{cwd}")

# contents = os.listdir(cwd)
# print(f"Contents:{contents}")

# os.mkdir("Python/mark4/data")
# print(f"data createed")

# os.chdir("/Python/mark4/data")
# new_cwd = os.getcwd()
# print(f"Current dir:{new_cwd}")

# with open("data.txt, w") as f:
#     f.write("mini")
# print(f"data.txt created")

# os.remove("data.txt")
# os.chdir("..")
# os.rmdir("data")
# print(f"data deleted")


#try 3
# def divide_number(a, b):
#     try:
#         result = a/b
#         return result
#     except ZeroDivisionError:
#         print("Cannot divide by zero")
#         return None
#     finally:
#         print("Operation completed")

# a = float(input("Enter 1st number(a): "))
# b = float(input("Enter 2nd number(b): "))

# result = divide_number(a, b)
# if result is not None:
#     print(f"Result of {a} / {b}: {result}")