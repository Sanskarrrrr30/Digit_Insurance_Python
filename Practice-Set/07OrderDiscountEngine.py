'''
7. Online Order Discount Engine 
Problem Statement 
Total order amount: 
● ≥ 5000 → 20% discount 
● ≥ 3000 → 10% 
● ≥ 1000 → 5% 
● Else → No discount 
Print final payable amount. 
Input: 
amount 
Output: 
payable_amount 
Sample Input: 
3200 
Sample Output: 
2880 
Hint: 
Apply only one highest applicable discount.
'''

amount=float(input("Enter order amount:    "))

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 3000:
    discount = amount * 0.10
elif amount >= 1000:
    discount = amount * 0.05
else:
    discount = 0

final_amount = amount - discount
print(f"Final Amount to Pay: ₹{final_amount:.2f}")
