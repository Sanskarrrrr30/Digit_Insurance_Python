'''
1. ATM Transaction Validator 
Problem Statement 
An ATM processes N withdrawal requests sequentially. 
Each request has an amount. Rules: 
● Withdrawal amount must be a multiple of 100 
● Account balance must never go negative 
● For each transaction, print SUCCESS or FAILED
Input 
InitialBalance 
N 
amount1 
amount2 
... 
amountN 
Output 
SUCCESS 
FAILED 
SUCCESS 
... 
FinalBalance 
Sample Input: 
5000 
4 
1200 
155 
2000 
2500 
 
Sample Output: 
SUCCESS 
FAILED 
SUCCESS 
FAILED 
1800 
 
Hint: 
Update balance only if both conditions are satisfied. 
'''

balance = input("Enter initial account balance: ")
balance = float(balance)
n = int(input("Enter number of withdrawal requests: "))

for i in range(n):
    amount = float(input(f"Enter withdrawal amount for request {i+1}: "))
    
    if amount % 100 != 0:
        print("FAILED: Amount must be a multiple of 100")
    elif amount > balance:
        print("FAILED: Insufficient balance")
    else:
        balance -= amount
        print("SUCCESS")
print(f"Remaining balance: {balance:.2f}")



