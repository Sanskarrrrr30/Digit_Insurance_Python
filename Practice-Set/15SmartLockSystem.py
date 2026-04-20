"""
15. Smart Door Lock System 
Problem Statement 
User gets 3 attempts to enter correct PIN. 
● Correct → ACCESS GRANTED 
● All wrong → LOCKED 
Input 
correct_pin 
attempt1 
attempt2 
attempt3 
 
Output 
ACCESS GRANTED / LOCKED 
 
Sample Input 
4321 
1111 
2222 
4321 
 
Sample Output 
ACCESS GRANTED 
 
Hint: 
Exit loop early on success.
"""

cp=input("Enter correct pin : ")
attempt=0
for i in range(3):
    attempt=input("Enter pin: ")
    if (attempt==cp):
        print("ACCESS GRANTED")
        break
