# PROG 6.2: Handling Exact User Error

try:
    num=int(input("Enter a number: "))

    result=100/num
    print("Result: ", result)

except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero. Please enter a non-zero number.")