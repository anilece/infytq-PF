

def find_new_salary(current_salary,job_level):
    # write your logic here3	15
    #4	7
    #5	5
    new_salary=0
    if(job_level==3):
        new_salary=current_salary+(current_salary*0.15)
    elif(job_level==4):
        new_salary=current_salary+(current_salary*0.07)
    elif(job_level==5):
        new_salary=current_salary+(current_salary*0.05)
    else:
        new_salary=-1
    new_salary=int(new_salary)
    return new_salary


new_salary=find_new_salary(15000,3)
print(new_salary)
