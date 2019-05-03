#PF-Assgn-23
def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    
    
    for i in range(len(reqd_gems)):
        for j in range(len(gems_list)):
            if (reqd_gems[i]==gems_list[j]):
                bill_amount+=(price_list[j]*reqd_quantity[i])
    for i in reqd_gems:
        if i not in gems_list:
            bill_amount=-1
    if (bill_amount>30000):
        bill_amount-=(bill_amount*0.05)
    return bill_amount


gems_list=['Amber', 'Aquamarine', 'Opal', 'Topaz']


price_list=[4316, 1342, 8734, 6421]


reqd_gems=['Amber', 'Topaz', 'Aquamarine']


reqd_quantity=[2, 3, 1]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)
