#PF-Assgn-20

def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):

    bank_emi_expected=0
    eligible_loan_amount=0
    if (account_number//1000!=1):
        print("Invalid account number")
    elif(account_balance<100000):
        print("Insufficient account balance")
    elif(account_number//1000==1 and account_balance>=100000):
            
        if(salary>100000 or loan_type=="Business" ):
            bank_emi_expected=84
            eligible_loan_amount=7500000
            if(bank_emi_expected>=customer_emi_expected
            and eligible_loan_amount>=loan_amount_expected):
                    print("Account number:", account_number)
                    print("The customer can avail the amount of Rs.", eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:",customer_emi_expected)
            elif(loan_amount_expected>eligible_loan_amount):
                print("The customer is not eligible for the loan")
            elif(salary<100000):
                print("Invalid loan type or salary")             
        elif(loan_type=="House"):
            if(salary<50000):
                print("Invalid loan type or salary")
            elif(salary>50000):
                eligible_loan_amount=5000000
                bank_emi_expected=60
                if(bank_emi_expected>=customer_emi_expected
                and eligible_loan_amount>=loan_amount_expected):
                        print("Account number:", account_number)
                        print("The customer can avail the amount of Rs.", eligible_loan_amount)
                        print("Eligible EMIs :", bank_emi_expected)
                        print("Requested loan amount:", loan_amount_expected)
                        print("Requested EMI's:",customer_emi_expected)
    
            
                elif(eligible_loan_amount<loan_amount_expected or bank_emi_expected<customer_emi_expected):
                    print("The customer is not eligible for the loan")
                    
        elif (salary>25000 and loan_type=="Car"):
            eligible_loan_amount=500000
            bank_emi_expected=36
            if(bank_emi_expected>=customer_emi_expected
            and eligible_loan_amount>=loan_amount_expected):
                    print("Account number:", account_number)
                    print("The customer can avail the amount of Rs.", eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:",customer_emi_expected)
            
            elif(loan_amount_expected>eligible_loan_amount or customer_emi_expected>bank_emi_expected):
                print("The customer is not eligible for the loan")
            elif(salary<=25000):
                print("Invalid loan type or salary")
                
        elif(salary<25000 or ( loan_type!="Car" or loan_type!="House" or loan_type!="Business")):
            print("Invalid loan type or salary")
        
        else:
            
            print("The customer is not eligible for the loan")

calculate_loan(1001,40000,250000,"Car",300000,30)
