#PF-Tryout

def generate_next_date(day,month,year):
    #Start writing your code here
    eve=[1,3,5,7,8,10]
    odd=[4,6,9,11]
    next_day=day
    next_month=month
    next_year=year
    if(day<31 and (month in eve)) or (day<30 and (month in odd)) or ((month==2) and day<28) :
        next_day=day+1
    elif(day==31 and (month in eve)) or (day==30 and (month in odd)) or (((day==28) or (day==29)) and month==2):
        next_day=1
        next_month=month+1
    elif(day==31 and month==12):
        next_day=1
        next_month=1
        next_year=year+1
        
    print(next_day,"-",next_month,"-",next_year)


generate_next_date(31,1,2015)
