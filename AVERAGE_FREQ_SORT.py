#PF-Assgn-35

#Global variable
list_of_marks=(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

def find_more_than_average():
    average=0
    for i in list_of_marks:
        average+=i
    average=average/10
    average_count=0
    for i in list_of_marks:
        if (i>average):
            average_count+=1
    return(int((average_count/10)*100))
  
def sort_marks():
    sorted_list=[]
    list_marks=list(list_of_marks)
    while (list_marks):
            minimum=list_marks[0]
            for i in list_marks:
                if i<minimum:
                  minimum=i
            sorted_list.append(minimum)
            list_marks.remove(minimum)
    return(sorted_list)    
        
   

def generate_frequency():
    list_marks=[]
    list_marks=list(list_of_marks)
    maximum=max(list_marks)
    frequency=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in (list_marks):
        frequency[i]+=1
    return(frequency)

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
