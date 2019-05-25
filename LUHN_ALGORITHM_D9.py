
def validate_credit_card_number(card_number):
    
    odd_list=[]
    req_list=list(str(card_number))
    for i in range(0,len(req_list),2):
        odd_list.append(req_list[i])
        req_list[i]=0
    print(odd_list,req_list)    
    for i in range(len(odd_list)):
        z=2*int(odd_list[i])
        if (z)>9:
            temp=0
            z=str(z)
            for j in z:
                temp+=int(j)
            odd_list[i]=temp
        else:
            odd_list[i]=int(odd_list[i])*2
    print(odd_list,req_list)   
    sum1=0
    for i in odd_list:
        sum1+=i
        print(sum1,odd_list, i)
    sum2=0
    for i in req_list:
        sum2+=int(i)
        print(sum2,req_list, i)
    if ((sum2+sum1)%10==0):
        return(True)
    else:
        return(False)
    
    
    
        
card_number= 5239512608615007 
#4539869650133101  #1456734512345698 # #5239512608615007
result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")
