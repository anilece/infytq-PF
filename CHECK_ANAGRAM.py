
def check_anagram(data1,data2):
    
    data1_list=list(data1.lower())
    data2_list=list(data2.lower())
    count=0
    flag="True"
    for i in data1_list:
        if i not in data2_list:
                flag="False"
                break
    for i in data2_list:
        if i not in data1_list:
            flag="False"
            break
    if (flag=="True"):        
        if len(data2)==len(data1):
            for i in range(len(data1_list)):
                temp=data2_list.index(data1_list[i])
           
                if (data1_list[i] in data2_list) and (i!=temp) and data1_list[i]==data2_list[temp]:
                            count+=1
                           
                            
            if count==len(data1):
                    return(True)
            else:
                    return(False)

        else:
            return (False)
    elif(flag=="False"):
        return(False)
print(check_anagram('resell','scller'))
