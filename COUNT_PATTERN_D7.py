#PF-Exer-35

def count_names(name_list):
    count1=0
    count2=0
    for i in name_list:
        if(len(i)==3 and i[-2]+i[-1]=="at"):
            count1+=1
    for i in range(len(name_list)):
        temp=name_list[i]
        for j in range(len(temp)-1):
            if (temp[j]+temp[j+1])=='at':
                count2+=1
   
    print("_at -> ",count1)
    print("%at% -> ",count2)



name_list=["Hat","Cat","rabbit","matter"]
count_names(name_list)
