
def calculate_loan_emi(principal, rate, time):
    # function to calculate EMI based on the principal amount, rate of interest, and time period
    rate = float(rate) / 1200 # convert annual interest rate to monthly rate
    emi = (float(principal) * rate * ((1 + rate) ** float(time))) / (((1 + rate) ** float(time)) - 1)
    return emi

def calculate_interest(principal, rate, time):
    # function to calculate the total interest payable based on the principal amount, rate of interest, and time period
    rate = float(rate) / 1200 # convert annual interest rate to monthly rate
    interest = float(principal) * rate * float(time)
    return interest


# Get user input for loan type
credit_score = int(input("Enter Your Credit Score : "))
if credit_score < 500:
    print("Sorry, you are not eligible for Any kind of loan as your credit score is too Low, consult with your respective Bank !")
    print("*To get loan approval you need minimum 500 credit score.")
    exit()
else:    
    print("Please select the type of loan you are interested in:")
    print("1. Home Loan")
    print("2. Personal Loan")
    print("3. Car Loan")
    loan_type = int(input("Enter the loan type (1, 2, or 3): "))

# Get user input for loan amount and tenure
    loan_amount = float(input("Enter the loan amount (in Rupees): "))
    loan_tenure = float(input("Enter the loan tenure (in months): "))
    interest_rate = float(input("Enter the interest rate (in percentage): "))

# Determine eligibility based on loan type and user input
    if loan_type == 1:
    # Home Loan eligibility criteria
        eligible_amount = 5000000 # maximum loan amount
        eligible_tenure = 360 # maximum loan tenure in months
        eligible_rate = 8.5 # interest rate
    elif loan_type == 2:
    # Personal Loan eligibility criteria
        eligible_amount = 2000000 # maximum loan amount
        eligible_tenure = 60 # maximum loan tenure in months
        eligible_rate = 12 # interest rate
    elif loan_type == 3:
    # Car Loan eligibility criteria
        eligible_amount = 3000000 # maximum loan amount
        eligible_tenure = 84 # maximum loan tenure in months
        eligible_rate = 9 # interest rate
    else:
        print("Invalid loan type selected!")
        exit()

    if loan_amount > eligible_amount:
        print("Sorry, you are not eligible for the requested loan amount!")
    elif loan_tenure > eligible_tenure:
        print("Sorry, you are not eligible for the requested loan tenure!")
    else:
        print("Congratulations, you are eligible for the requested loan!")
        sanctioned_amount = loan_amount
        sanctioned_tenure = loan_tenure
        sanctioned_rate = interest_rate
        total_interest = calculate_interest(sanctioned_amount, sanctioned_rate, sanctioned_tenure)
        total_amount = sanctioned_amount + total_interest
        emi = calculate_loan_emi(sanctioned_amount, sanctioned_rate, sanctioned_tenure)
        print("Sanctioned Amount: ", sanctioned_amount)
        print("Sanctioned Tenure: ", sanctioned_tenure)
        print("Sanctioned Interest Rate: ", sanctioned_rate)
        print("Total Interest Payable: ", total_interest)
        print("Total Payable Amount: ", total_amount)
        print("Monthly EMI: ", round(emi, 2))





