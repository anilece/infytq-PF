#PF-Assgn-19

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    #write your logic here
    if(food_type=='N' and distance_in_kms>0):
        bill_amount=150*quantity_ordered
        if(distance_in_kms>3 and distance_in_kms<=6):
            bill_amount+=(3*(distance_in_kms-3))
        elif(distance_in_kms>6):
            bill_amount+=((3*3)+((distance_in_kms-6)*6))
        else:
            bill_amount=bill_amount
    elif(food_type=="V" and distance_in_kms>0):
        bill_amount=120*quantity_ordered
        if(distance_in_kms>3 and distance_in_kms<=6):
            bill_amount+=(3*(distance_in_kms-3))
        elif(distance_in_kms>6):
            bill_amount+=((3*3)+((distance_in_kms-6)*6))
        else:
            bill_amount=bill_amount
    else:
        bill_amount=-1
    if (quantity_ordered<1):
        bill_amount=-1
    else:
        bill_amount=bill_amount
    return bill_amount


bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)
