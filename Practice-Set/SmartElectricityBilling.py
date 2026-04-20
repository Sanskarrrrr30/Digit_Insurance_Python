"""
2. Smart Electricity Billing 
Problem Statement 
Electricity bill is calculated slab-wise: 
● First 100 units → ₹3/unit 
 
● Next 100 units → ₹5/unit 
 
● Remaining → ₹8/unit 
 
If usage > 300 units, add 10% surcharge.
"""

units=float(input("Enter total electricity units consumed: "))
if units <= 100:
    bill = units * 3
elif units <= 200:
    bill = (100 * 3) + ((units - 100) * 5)
else:
    bill = (100 * 3) + (100 * 5) + ((units - 200) * 8)

# Add 10% surcharge
if units > 300:
    bill += bill * 0.10  

print(f"Total electricity bill: ₹{bill:.2f}")