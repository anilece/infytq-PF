#PF-Assgn-46

res_list=[0]
def nearest_palindrome(number): 
    res=''
    number+=1
    temp=list(str(number))
    flag=True
    while(flag):
            for i in range(len(temp)):
                    temp[i]=int(temp[i])
                    temp[-i-1]=int(temp[-i-1])
                    if (len(temp)%2==0):
                        if temp[i]==temp[-i-1]:
                            temp[i]=temp[-i-1]
                        elif(temp[i]<temp[-i-1]):
                            temp[-i-1]=temp[i]
                        elif(temp[i]>temp[-i-1]):
                            temp[i]=temp[-i-1]
                    else:
                            if( temp[i]==temp[-i-1] and i!=0):
                                temp[-i-1]=temp[i]
                            elif(temp[i]<temp[-i-1]):
                                temp[-i-1]=temp[i]
                            elif(temp[i]>temp[-i-1]):
                                temp[i]=temp[-i-1]
            for i in temp:
                res+=str(i)
            result=int(res)
            if result in res_list :
                pass
            else:
                res_list[0]=result

            flag=False
            if (result<number):
                nearest_palindrome(number)

    return(res_list[0])



number=1236789
ress=nearest_palindrome(number)
print(ress)



