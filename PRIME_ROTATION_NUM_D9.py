
import math
def check_prime(number):
    c=0
    for i in range(2,int(math.sqrt(number))+1):
        if number%i==0:
            c=1
    if c==1:
        return(False)
    else:
        return(True)
    

def rotations(num):
    temp=num
    a=str(num)
    res=[]
    tmp=str(num)
    for i in range(0,len(a)):
        
        res.append(int(tmp))
        tmp=''
        for i in range(len(a)):
            if i!= len(a)-1:
                tmp+=a[i+1]
            else:
                tmp+=a[0]
        
        a=tmp
        
            
    return(res)
    

     

def get_circular_prime_count(limit):
    count=0
    if limit<2:
        count=0
    else:
        for i in range(2,limit):
            c=0
            a=rotations(i)
            for i in a:
                if (check_prime(i)):
                    c+=1
            if c==len(a):
                count+=1
    return(count)            
   
print(get_circular_prime_count(197))
print(rotations(179))
