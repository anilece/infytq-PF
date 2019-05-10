#PF-Assgn-43

def find_smallest_number(num):
   
    for val in range(1,1000):
        res=[]
        for numm in range(1,val+1):
            if val%numm==0:
                res.append(numm)
        if len(res)==num:
            return val
            
num=16
print("The number of divisors :",num)

result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)
