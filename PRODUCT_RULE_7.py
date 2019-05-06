#PF-Assgn-15

def find_product(num1,num2,num3):
    product=0
    if (num1==7):
        product=num2*num3
    elif(num2==7):
        product=num3
    elif(num3==7):
        product=-1
    else:
        product=num1*num2*num3
    #write your logic here
    return product


product=find_product(7,6,2)
print(product)
