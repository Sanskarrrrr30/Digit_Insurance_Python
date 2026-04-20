"""
13. Train Ticket Fare Calculator 
Problem Statement 
Fare rules: 
● Distance × ₹2/km 
 
● Senior citizen → 30% discount 
 
● Child (<12) → 50% discount 
 
Input 
distance 
age 
 
Output 
fare 
 
Sample Input 
200 
65 
 
Sample Output 
280 
 
Hint: 
Calculate base fare first, then apply age-based rule.
"""


dis=float(input("Enter Distance: "))
age=int(input("Enter Age: "))
fare=dis*2
if age>=60:
    dic=fare*0.30
elif age<12:
    dic=fare*0.50
else:
    dic=0
final_fare=fare-dic
print(final_fare)