"""
4. Number Pattern Validator 
Problem Statement 
Check if digits of a number are strictly increasing left to right. 
Input 
number 
Output 
YES / NO 
Sample Input 
13579 
Sample Output 
YES 
Hint: 
Compare adjacent digits.
"""

num=input("Enter a number :  ")
is_increasing=True
for i in range(len(num)-1):
    if num[i] >= num[i+1]:
        is_increasing=False
        break
if is_increasing:
    print("YES")
else:    print("NO")
