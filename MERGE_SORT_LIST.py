#PF-Exer-29
def merge_lists(list1,list2):
    #Write your logic here
    new_merge_list=[]
    for i in range(len(list1)+len(list2)):
        
        if(i<len(list1)):
           new_merge_list.append(list1[i])
        elif(i>=len(list1)):
            new_merge_list.append(list2[i-len(list1)])
            
    return new_merge_list
def sort_list(merged_list):
    #Write your logic here
    sorted_merged_list=[]
    
    while (len(merged_list)!=0):
        minimum = merged_list[0]   
        for x in merged_list: 
             if (x <= minimum):
                   minimum = x
        sorted_merged_list.append(minimum)
        merged_list.remove(minimum)
       
    return sorted_merged_list

merged_list=merge_lists(list1= [3],list2= [77,88,99])
print(merged_list)
sorted_merged_list=sort_list(merged_list)
print(sorted_merged_list)
