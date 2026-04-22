"""
18. Bus Seat Allocation 
Problem Statement 
Bus has 40 seats. For each booking request: 
● If seats available → CONFIRMED 
 
● Else → WAITLISTED 
 
Input 
N 
request1 
request2 
... 
 
Output 
CONFIRMED / WAITLISTED 
 
Sample Input 
3 
15 
10 
20 
 
 
 
Sample Output 
CONFIRMED 
CONFIRMED 
WAITLISTED 
Hint: 
Track remaining seats.
"""

total_seats = 40
n = int(input("Enter number of booking requests: "))
for i in range(n):
    request = int(input(f"Enter number of seats requested for booking {i+1}: "))
    if request <= total_seats:
        print("CONFIRMED")
        total_seats -= request
    else:
        print("WAITLISTED")

    