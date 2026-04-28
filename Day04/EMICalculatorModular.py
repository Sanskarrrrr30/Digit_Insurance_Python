def calculate_interest(principal, rate, time):
    return (principal * rate * time) / 100

def calculate_emi(principal, annual_rate, time_years):
    monthly_rate = annual_rate / (12 * 100)
    months = time_years * 12
    emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    return emi

def print_emi_schedule(principal, annual_rate, time_years):
    monthly_rate = annual_rate / (12 * 100)
    months = time_years * 12
    emi = calculate_emi(principal, annual_rate, time_years)
    balance = principal
    
    print("\nMonth\tEMI\t\tPrincipal Paid\tInterest Paid\tRemaining Balance")
    for month in range(1, int(months) + 1):
        interest_paid = balance * monthly_rate
        principal_paid = emi - interest_paid
        balance -= principal_paid
        print(f"{month}\t{emi:.2f}\t\t{principal_paid:.2f}\t\t{interest_paid:.2f}\t\t{balance:.2f}")
    
def main():
    principal = float(input("Enter the principal amount: "))
    annual_rate = float(input("Enter the annual interest rate (in %): "))
    time_years = float(input("Enter the time period (in years): "))
    
    emi = calculate_emi(principal, annual_rate, time_years)
    print(f"The EMI for the given loan is: {emi:.2f}")
    
    print_emi_schedule(principal, annual_rate, time_years)

if __name__ == "__main__":
    main()