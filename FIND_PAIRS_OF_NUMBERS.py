#PF-Assgn-34
def find_pairs_of_numbers(num_list,n):
    count=0
    for i in range(len(num_list)):
        temp=i
        for j in range(len(num_list)):
            if (num_list[i]+num_list[j]==n) and (i!=j):
                count+=1
                num_list[i]=0
                num_list[j]=0
                
    return(count)
    

num_list=[1, 2, 4, 5, 6]
n=6
print(find_pairs_of_numbers(num_list,n))
