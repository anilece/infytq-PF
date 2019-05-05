#PF-Exer-26

def factorial(number):
   
    fact=1
    if (number==0):
        return 1
    while(number!=0):
        fact*=number
        number-=1
    return fact

def find_strong_numbers(num_list):
  
    res_list=[]*len(num_list)
    temp_list=[0]*len(num_list)
    for i in range(len(num_list)):
        temp=num_list[i]
        temp_list[i]=0
        if temp==0:
            temp_list[i]=factorial(temp)
        while(temp!=0):
            rem=temp%10
            temp=temp//10
            temp_list[i]+=factorial(rem)
    for i in range(len(num_list)):
        if(num_list[i]==temp_list[i]):
            res_list.append(num_list[i])
    if len(res_list)==0:
        return (-1)
    else:    
        return res_list

num_list=[100,20,40]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)
