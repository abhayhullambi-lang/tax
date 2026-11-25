# Tax Calculator

# Function to calculate taxable income
def taxable_income(inc):
    if inc < 0:
        raise ValueError("Income cannot be negative")
    return inc


# Function to calculate tax
def tax(inc):
    inc = taxable_income(inc)

    if inc <= 250000:
        return 0
    elif inc <= 500000:
        return (inc - 250000) * 0.05
    elif inc <= 1000000:
        return (250000 * 0.05) + (inc - 500000) * 0.20
    else:
        return (250000 * 0.05) + (500000 * 0.20) + (inc - 1000000) * 0.30


# Function to calculate net income
def net_income(inc):
    return inc - tax(inc)


# Main function
def main():
    print("===== TAX CALCULATOR =====")

    inc = float(input("Enter your annual income: "))

    print("\n----- TAX DETAILS -----")
    print("Annual Income: Rs.", inc)
    print("Taxable Income: Rs.", taxable_income(inc))
    print("Income Tax: Rs.", tax(inc))
    print("Net Income: Rs.", net_income(inc))


if __name__ == "__main__":
    main()