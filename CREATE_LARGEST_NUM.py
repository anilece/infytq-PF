#PF-Assgn-36
def create_largest_number(number_list):
    
    temp=[]
    result=''
    while(number_list):
        maximum=number_list[0]
        for i in number_list:
            if i//100==0:
                if i>maximum:
                    maximum=i
            else:
                return 0
        temp.append(maximum)
        number_list.remove(maximum)
        
    for i in temp:
        temmp=str(i)
        result+=temmp
    return(int(result))


number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
