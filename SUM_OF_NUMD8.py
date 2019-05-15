#PF-Assgn-52

import random
def sum_of_numbers(list_of_num,filter_func=None):
    
    if (filter_func!=None):
        res_sum=0
        listt=[]
        if(filter_func==odd(list_of_num)):
            listt=odd(list_of_num)
        elif(filter_func==even(list_of_num)):
            listt=even(list_of_num)
        for i in listt:
            
                res_sum+=i
        return(res_sum)
    else:
        res_sum=0
        for i in list_of_num:
            res_sum+=i
        return(res_sum)
def even(data):
     
    even_lst=[i for i in data if i%2==0]
    return(even_lst)
def odd(data):
     
    odd_lst=[i for i in data if i%2==1]
    return(odd_lst)
sample_data = range(1,11)
func=random.choice([odd(sample_data),even(sample_data),None])
print(sum_of_numbers(sample_data,func))
