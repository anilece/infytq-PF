#PF-Tryout

def FIND_BALANCE_AMOUNT_DEPOSIT(value,balance,amount):
        balance=balance_list[value]
        new_balance=balance+amount
        if(new_balance >= 500):
            balance_list[value]=new_balance
            print("Transaction completed successfully")
            print("Balance Amount :", new_balance)
                
def FIND_BALANCE_AMOUNT_WITHDRAW(value,balance,amount,balance_list):
        balance=0
        balance=balance_list[value]
        new_balance=balance-amount
        if(new_balance >= 500):
            balance_list[value]=new_balance
            print("Transaction completed successfully")
            print("Balance Amount :", new_balance)
        else:
            print("Insufficient Balance")
def FIND_ACC_IN_LIST(account_number,account_list):
        
        for index in range(0,len(account_list)):
             
             if(account_list[index]==account_number):
               
                value=index
                return value       
        else:
                value=0
                
def TRANSACTION_TYPE(transaction_type,account_number,account_list,amount,balance_list):
    balance=0
    if(transaction_type=="Withdraw"):
        flag=FIND_ACC_IN_LIST(account_number,account_list)
     
        if(flag!=0):
            value=flag
            
            FIND_BALANCE_AMOUNT_WITHDRAW(value,balance,amount,balance_list)
        else:
             print("Invalid Account number")

    elif(transaction_type=="Deposit"):
        flag=FIND_ACC_IN_LIST(account_number,account_list)
        if(flag==True):
           FIND_BALANCE_AMOUNT_DEPOSIT(value,balance,amount)
       
    elif(transaction_type=="Balance Enquiry"):
        flag=FIND_ACC_IN_LIST(account_number,account_list)
        if(flag==True):
            balance=balance_list[value]
            print(balance)
        else:
            print("Invalid Account number")
    else:
         print("Invalid Transaction Type")
value=0    
account_list=[1001,1002,1003,1004,1005]
balance_list=[2500,10000,7000,1500,500]
amount=1000
account_number=1003
transaction_type="Withdraw"
TRANSACTION_TYPE(transaction_type,account_number,account_list,amount,balance_list)
