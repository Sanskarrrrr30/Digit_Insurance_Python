#PROG 4.2 : Function Annotation

def add_numbers(a: int, b: int) -> int:
    """This function takes two integers and returns their sum."""
    return a + b

sum1 = add_numbers(10, 20)
sum2 = add_numbers(30, 40)
print("Sum 1: ", sum1)
print("Sum 2: ", sum2)

