'''
9.Mobile Battery Drain Simulator
Problem Statement 
Battery starts at 100%. Each app drains fixed % per minute. 
Stop when battery ≤ 0. Print minutes used. 
Input: 
drain_per_minute 
Output: 
minutes 
Sample Input 
7 
Sample Output 
15 
Hint: 
Use a loop until battery <= 0.
'''
drainperminute = int(input())

battery = 100
minutes = 0

while battery > 0:
    battery -= drainperminute
    minutes += 1

print(minutes)