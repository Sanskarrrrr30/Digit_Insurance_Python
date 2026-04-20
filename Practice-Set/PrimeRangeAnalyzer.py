"""
6. Prime Range Analyzer 
Problem Statement 
Print count of prime numbers between A and B (inclusive). 
Input: 
A 
B 
 
Output: 
prime_count 
 
Sample Input: 
10 
30 
 
Sample Output: 
6 
 
Hint: 
Check divisibility up to √n.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

num1 = int(input("Enter the starting number: "))
num2 = int(input("Enter the ending number: "))
count = 0
for num in range(num1, num2 + 1):
    if is_prime(num):
        count += 1
print(f"Count of prime numbers between {num1} and {num2} is: {count}")


# print("Prime numbers between", num1, "and", num2, "are:")
# for num in range(num1, num2 + 1):
#     if is_prime(num):
#         print(num, end=" ")

