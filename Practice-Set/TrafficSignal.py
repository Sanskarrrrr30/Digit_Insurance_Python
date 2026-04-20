"""
4. Traffic Signal Simulation 
Problem Statement 
A signal cycles every second: 
● 1–30 → RED 
● 31–45 → YELLOW 
● 46–90 → GREEN 
Given a time T, print the signal color. 
Input: 
T 
Output: 
RED / YELLOW / GREEN 
Sample Input: 
44 
Sample Output: 
YELLOW 
 
Hint: 
Use modulo arithmetic and range checks. 
"""

T = int(input("Enter time in seconds: "))
cycle_time = T % 90
if 1 <= cycle_time <= 30:
    print("RED")
elif 31 <= cycle_time <= 45:
    print("YELLOW")
elif 46 <= cycle_time <= 90:
    print("GREEN")
