def check_positive_number(a):

    if a < 0:
        raise ValueError("The number must be positive!")
    return a
def getInput():
    try:
        a = int(input("Enter any value: "))
        check_positive_number(a)
        print ("The number is positive!")
    except ValueError as e:
        print(e)

getInput()