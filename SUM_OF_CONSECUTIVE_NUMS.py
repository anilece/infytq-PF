#PF-Assgn-42
def find_factors(num):
 
    factors = []
    for i in range(2,(num+1)):
        if(num%i==0):
            factors.append(i)
    return factors

def is_prime(num, i):
  
    if(i==1):
        return True
    elif(num%i==0):
        return False;
    else:
        return(is_prime(num,i-1))

def find_largest_prime_factor(list_of_factors):
    re=[]
    for i in list_of_factors:
        a=is_prime(i,i//2)
        if (a):
            re.append(i)
    if(len(re)>0):
        maxx=max(re)
        return( maxx)
    else:
        return(0)
    

def find_f(num):
    factor_list=find_factors(num)
    numm=find_largest_prime_factor(factor_list)
    return(numm)
    
   

def find_g(num):
    num_list=[0]
    sum=0
    i=1
    while(i <=9):
        num_list.append(num)
        res=find_f(num_list[i])
        sum+=res
        i+=1
        num+=1
    return(sum)
    
        
   

print(find_g(78))
