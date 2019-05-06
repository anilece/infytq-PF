#PF-Assgn-33

def find_common_characters(msg1,msg2):
   
    result_list=[]
    for i in range(len(msg1)):
        for j in range(len(msg2)):
            if (msg1[i]==msg2[j]):
                result_list.append(msg1[i])
                break
    result_str=''
    for i in result_list:
        result_str+=i
    if len(result_str)==0:
        return -1
    else:    
        return(result_str)    

msg1="moto"
msg2="moto"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
