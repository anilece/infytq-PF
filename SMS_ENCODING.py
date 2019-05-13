#PF-Assgn-50

def sms_encoding(data):
    #start writing your code here
    data_list=[]
    temp=''
    for i in range(len(data)):
        if data[i]!=" ":
            temp+=data[i].lower()
        elif data[i]==" ":
            data_list.append(temp)
            temp=''
        if i==len(data)-1:
            data_list.append(temp)
    
    vowels=['a','e','i','o','u']
    res=[]
    re=''
    for i in data_list:
        temp=list(i)
        if len(temp)==1:
            if i in vowels:
                re+=i
                
        for j  in temp:
                if j not in vowels:
                    re+=j
        
        re+=' ' 
    res.append(re)
    result=''
    for i in range(len(res)):
        temp=list(res[i])
        for i in range(len(temp)):
            if (i!=len(temp)-1):
                 result+=temp[i]
        
    return(result)
                
data="GOOD DAYS AND BAD DAYS"
print(sms_encoding(data))
