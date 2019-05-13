#PF-Assgn-48

def find_correct(word_dict):
    
    keys=[]
    values=[]
    for i in word_dict.keys():
        keys.append(i)
    for i in word_dict.values():
        values.append(i)
    c_1=0
    c_2=0
    c_3=0

    for k in range(len(keys)):
        list_k=[]
        list_v=[]
        list_k=list(keys[k])
        list_v=list(values[k])
        count=0
        for j in range(len(list_k)):
            if(len(list_v)!=len(list_k)):
                c_3+=1
                break
            else:
                if list_k[j]!=list_v[j]:
                    count+=1
            
        if (count==0 and (len(list_v)==len(list_k))):
            c_1+=1
        elif(count==2 or count==1) and (len(list_v)==len(list_k)):
            c_2+=1
        elif(count>2 ):
            c_3+=1
    result=[c_1,c_2,c_3]
    return(result)
    
word_dict={'CHECK': 'CHEK', 'RADIO': 'RADICAL', 'MIND': 'MUND', 'VENDOR': 'VENDING', 'ALWAYS': 'ALLISWELL'}
print(find_correct(word_dict))
