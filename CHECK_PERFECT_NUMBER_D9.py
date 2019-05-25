
def check_perfect_number(number):
    
    sum=0
    for i in range(1,number):
        if number%i==0:
            sum+=i
    if sum==number:
        return(True)
    else:
        return(False)
def check_perfectno_from_list(no_list):
     
    result=[]
    for i in no_list:
        if check_perfect_number(i):
            result.append(i)
    return(result)        

perfectno_list=check_perfectno_from_list([18,6,4,2,1,28,496])
print(perfectno_list)
