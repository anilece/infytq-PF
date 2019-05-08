#PF-Assgn-38

def check_double(number):
    number_str=str(number)
    number_list=list(number_str)
    double_num=number*2
    double_num_str=str(double_num)
    double_num_list=list(double_num_str)
    count=0
    for i in number_list:
        for j in double_num_list:
            if j==i:
                count+=1
    if(count==len(number_list)):
        return True
    else:
        return False



print(check_double(125874))
