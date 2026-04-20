binary=input("Enter a binary number: ")
decimal=0
for i in range(len(binary)):
    decimal += int(binary[len(binary)-1-i]) * (2 ** i)
print(f"The decimal value of {binary} is: {decimal}")