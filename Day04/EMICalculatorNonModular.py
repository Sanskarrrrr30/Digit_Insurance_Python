principal = input("Enter the principal amount: ")
rate = input("Enter the annual interest rate (in %): ")
time = input("Enter the time period (in years): ")
# Convert inputs to float
principal = float(principal)
rate = float(rate)
# Convert annual rate to monthly and percentage to decimal
interest_rate = rate / (12 * 100)  
time = float(time)
months = time * 12  # Convert years to months
# Calculate EMI
emi = (principal * interest_rate * (1 + interest_rate) ** months) / ((1 + interest_rate) ** months - 1)
print(f"The EMI for the given loan is: {emi:.2f}")
balance = principal
print("\nMonth\tEMI\t\tPrincipal Paid\tInterest Paid\tRemaining Balance")
for month in range(1, int(months) + 1):
    interest_paid = balance * interest_rate
    principal_paid = emi - interest_paid
    balance -= principal_paid
    print(f"{month}\t{emi:.2f}\t\t{principal_paid:.2f}\t\t{interest_paid:.2f}\t\t{balance:.2f}")


