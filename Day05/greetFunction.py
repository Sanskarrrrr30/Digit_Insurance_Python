def greet(name):
    if name.isalpha():
        print(f"Hello, {name}!")
    else:
        print("Invalid input. Please enter a valid name.")

name = input("Enter your name: ")
greet(name)