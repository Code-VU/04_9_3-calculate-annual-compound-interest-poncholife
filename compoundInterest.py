def calculateCompoundInterest():
    print("Compound Interest: "+ find_compound_interest())
    print('---')
    print("Compound Interest: "+ find_compound_interest())
    print('---')
    print("Compound Interest: "+ find_compound_interest())

def find_compound_interest():
    
    principle = float(input("Principle (amount): "))
    time =      float(input("Time:               "))
    rate =      float(input("Rate:               "))
 
    total_amount = (((rate/100) + 1)**time)*principle

    compound_interest = total_amount - principle
    compound_interest = round(compound_interest,2)
    
    return str(compound_interest)

    # end assignment

if __name__ == "__main__":
    calculateCompoundInterest()
    