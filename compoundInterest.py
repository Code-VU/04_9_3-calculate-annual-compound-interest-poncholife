def calculateCompoundInterest():
    single_calculation_of_compound_interest()
    print('---')
    single_calculation_of_compound_interest()
    print('---')
    single_calculation_of_compound_interest()

def single_calculation_of_compound_interest():    
    client_initial_principal = float(input("Principle (amount): "))
    client_time =      float(input("Time:               "))
    client_rate =      float(input("Rate:               "))

    client_ending_principal = client_initial_principal*((1+(client_rate/100))**client_time)
    client_compound_interest = client_ending_principal - client_initial_principal
    rounded_client_compound_interest = round(client_compound_interest, 2)
    print(f"Compound Interest: {rounded_client_compound_interest}")

## If you want to test locally run > python compoundInterest.py

if __name__ == "__main__":
    calculateCompoundInterest()

