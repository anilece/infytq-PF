#PF-Assgn-30

def encode(message):
    message_list=list(message)
    count=1
    result=""
    result_list=[]
    if(len(message_list)>1):
        for i in range(len(message_list)-1):
            if (message_list[i]==message_list[i+1]):
                count+=1
                if(i==len(message_list)-2):
                    result_list.append(count)
                    result_list.append(message_list[i])
            else:
                result_list.append(count)
                result_list.append(message_list[i])
                count=1
                if(i==len(message_list)-2):
                        result_list.append(count)
                        result_list.append(message_list[i+1])
                           
        for i in range(len(result_list)):
            temp=str(result_list[i])
            result+=temp
            
    else:
        result+="1"+message
    return(result)    
    

encoded_message=encode("ABBBBCCCCCCCCAA")
print(encoded_message)
