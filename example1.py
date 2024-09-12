'''
write a program compound interest

'''# Function to calculate compound interest
def calculate_compound_interest(principal, rate, time, n):
    # Calculate compound interest
    amount = principal * (1 + rate / (n * 100))**(n * time)
    compound_interest = amount - principal
    return compound_interest, amount

# Input values
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time (in years): "))
n = int(input("Enter the number of times interest is compounded per year: "))

# Calculate compound interest
compound_interest, amount = calculate_compound_interest(principal, rate, time, n)

# Print the results
print(f"\nCompound Interest: {compound_interest:.2f}")
print(f"Total Amount after {time} years: {amount:.2f}")

