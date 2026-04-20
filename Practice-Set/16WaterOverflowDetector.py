"""
16. Water Tank Overflow Detector 
Problem Statement 
Tank capacity is 1000L. Inflow every minute given. 
 Stop when overflow occurs and print minute number. 
Input 
N 
inflow1 inflow2 ... inflowN 
 
Output 
overflow_minute 
 
Sample Input 
5 
200 300 250 400 100 
Sample Output 
4 
Hint : 
Accumulate volume gradually.
"""

n=int(input())
tank=1000
min=0
total=0
filled_time=-1

for i in range(n):
    inflow=int(input())
    total+=inflow
    min+=1
    if total>=tank and filled_time==-1:
        filled_time=min
        
        
print(filled_time)