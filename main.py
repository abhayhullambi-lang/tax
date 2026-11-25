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
        return 12500 + (inc - 500000) * 0.20
    else:
        return 112500 + (inc - 1000000) * 0.30


# Function to calculate net income
def net_income(inc):
    return inc - tax(inc)


# NEW FEATURE: Function to identify income category
def tax_category(inc):
    if inc < 0:
        raise ValueError("Income cannot be negative")
    elif inc <= 250000:
        return "No Tax Category"
    elif inc <= 500000:
        return "Low Income Category"
    elif inc <= 1000000:
        return "Middle Income Category"
    else:
        return "High Income Category"


# Main function
def main():
    print("===== TAX CALCULATOR =====")

    inc = float(input("Enter your annual income: "))

    print("\n----- TAX DETAILS -----")
    print("Annual Income: Rs.", inc)
    print("Taxable Income: Rs.", taxable_income(inc))
    print("Income Tax: Rs.", tax(inc))
    print("Net Income: Rs.", net_income(inc))
    print("Income Category:", tax_category(inc))


if __name__ == "__main__":
    main()