"""
11. Number Compression Counter 
Problem Statement 
Given a number, count how many times it can be divided by 2 until it becomes odd. 
Input 
number 
Output 
count 
Sample Input 
40 
Sample Output 
3 
Hint: 
Use a loop and modulo check.
"""
n=int(input("N: "))
count=0
while n%2==0:
    n=n//2
    count+=1
print(count)
