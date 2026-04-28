# PROG 6.1: Handling User Error

try:
    num=int(input("Enter a number: "))

    result=100/num
    print("Result: ", result)

except:
    print("Error occurred. Please enter a valid number.")