def carLoanPayement(P,Y,R):
    r=R/100/12
    n=Y*12
    M=(P*r*(1+r)**n)/((1+r)**n-1)
    monthly_payment = M
    total_payment = monthly_payment * Y * 12
    print(f"Monthly Payment: {monthly_payment:.2f}")
    print(f"Total Payment: {total_payment:.2f}")


P = float(input("Enter the principal amount: "))
Y = int(input("Enter the number of years: "))
R = float(input("Enter the annual interest rate (in %): "))
carLoanPayement(P, Y, R)