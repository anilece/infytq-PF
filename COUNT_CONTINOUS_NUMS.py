#PF-Exer-18

def get_count(num_list):
    count=0

   
    for i in range(len(num_list)-1):
        if num_list[i]==num_list[i+1]:
            count+=1
            i=i+1

    return count


num_list=[1,1,5,100,-20,-20,6,0,0]
print(get_count(num_list))
