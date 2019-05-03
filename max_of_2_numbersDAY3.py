#PF-Assgn-28

def find_max(num1, num2):
    num_list=[]
    max_num=-1
    digit_sum1=0
    digit_sum2=0
    num1_no_of_digits=0
    num2_no_of_digits=0
    while(num1!=0 or num2!=0):
        digit_sum1+=num1%10
        num1=num1/10
        num1_no_of_digits+=1
        digit_sum2+=num2%10
        num2/=10
        num2_no_of_digits+=1
    if(digit_sum2%3==0 and digit_sum1%3==0) and (num1<num2):
        if(num1_no_of_digits<=2 and num2_no_of_digits<=2):
            if(num1%5==0 and num2%5==0):
               num_list.append(num1,num2)
            else:
                max_num=-1
        else:
            max_num=-1
    else:
        max_num=-1
    if (max_num!=-1):
        max_num=max(num_list)
    # Write your logic here
    return max_num


max_num=find_max(10,15)
print(max_num)
