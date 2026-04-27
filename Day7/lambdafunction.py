# given list, create a new list with doubled values using lambda function

# Lambda Function
# str1="Internship"
# upper = lambda s: s.upper()
# print(upper(str1))

# maxi=lambda a,b: a if a > b else b
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# print(maxi(num1, num2))

# Map Function
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
square = list(map(lambda x: x ** 2, numbers))
cube = list(map(lambda x: x ** 3, numbers))

print(doubled)
print(square)
print(cube)
