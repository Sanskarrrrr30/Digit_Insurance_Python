'''
8. Binary to Decimal Converter (Without Built-in) 
Problem Statement 
Given a binary number, convert to decimal. 
Input: 
binary_number 
Output: 
decimal_number 
Sample Input: 
101101 
Sample Output: 
45 
Hint: 
Process digits from right to left using powers of 2.
'''
binary=input("Enter a binary number: ")
decimal=0
for i in range(len(binary)):
    decimal += int(binary[len(binary)-1-i]) * (2 ** i)
print(f"The decimal value of {binary} is: {decimal}")