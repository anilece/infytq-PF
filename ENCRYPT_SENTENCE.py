#PF-Assgn-47
def encrypt_sentence(sentence):
    #start writing your code here
    sen_list=[]
    temp=''
    res=[]
    for i in range(len(sentence)):
        
        if sentence[i]==" ":
            temp=temp
            sen_list.append(temp)
            temp=''
        elif i==len(sentence)-1:
            temp+=sentence[i]
            sen_list.append(temp)
        else:
            temp+=sentence[i]
    
    re_list=['']*len(sen_list)
    for i in range(len(sen_list)):
        if i%2==0:
            temp=sen_list[i]
            temp=list(temp)
            temp.reverse()
            st=''
            for k in temp:
                st+=k
           
            re_list[i]=st
        else:
            vowels=['a','e','i','o','u']
            temp=sen_list[i]
            c=''
            v=''
            for j in temp:
                if j not in vowels:
                    c+=j
                else:
                    v+=j
           
            re_list[i]=c+v
    result=''
    for i in range(len(re_list)):
        if i==(len(re_list)-1):
            result+=re_list[i]
        else:
            result+=re_list[i]+" "
   
    return(result)
sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
