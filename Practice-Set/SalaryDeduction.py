"""
5. Salary Deduction System 
Problem Statement 
Employee salary rules: 
● Basic salary given 
 
● If late days > 5 → deduct 5% 
 
● If late days > 10 → deduct 10% 
 
● If absent days > 2 → deduct additional 5% 
 
Input: 
salary 
late_days 
absent_days 
 
Output: 
final_salary 
 
Sample Input: 
50000 
8 
1 
 
Sample Output: 
47500 
 
Hint: 
Apply deductions cumulatively, not exclusively.
"""

salary=float(input("Salary: "))
late=int(input("Late days: "))
absent=int(input("Absent days: "))
final_sal=salary

if late > 10:
    final_sal -= salary * 0.10
elif late > 5:
    final_sal -= salary * 0.05
if absent > 2:
    final_sal -= salary * 0.05

print(f"Final Salary: {final_sal:.2f}")
