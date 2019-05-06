#PF-Assgn-32
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    medical_speciality_list=[]
    for i in range(0,len(patient_medical_speciality_list),2):
            medical_speciality_list.append(patient_medical_speciality_list[i+1])
    
    count_list=[0]*3
    for i in medical_speciality_list:
        if i=="P":
            count_list[0]+=1
        elif i=="O":
            count_list[1]+=1
        elif i=="E":
            count_list[2]+=1
    medical_list=["P","O","E"]
    maxx=max(count_list)
    for i in range(len(count_list)):
        if count_list[i]==maxx:
            temp=i
            result=medical_list[temp]
    return(medical_speciality[result])        

patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
