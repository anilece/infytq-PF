
ticket_list=["AI567:MUM:LON:014","AI077:MUM:LON:056", "BA896:MUM:LON:067", "SI267:MUM:SIN:145","AI077:MUM:CAN:060","SI267:BLR:MUM:148","AI567:CHE:SIN:015","AI077:MUM:SIN:050","AI077:MUM:LON:051","SI267:MUM:SIN:146"]

def find_passengers_flight(airline_name="AI"):
    #This function finds and returns the number of passengers travelling in the specified airline.
    count=0
    for i in ticket_list:
        string_list=i.split(":")
        if(string_list[0].startswith(airline_name)):
            count+=1
    return count

def find_passengers_destination(destination):
    
    temp=destination
    c=0
    for i in range(len(ticket_list)):
        tp=ticket_list[i][10:13]
        if tp==temp:
            c+=1
    return(c)        
   
def find_passengers_per_flight():
    '''Write the logic to find and return a list having number of passengers traveling per flight based on the details in the ticket_list
    In the list, details should be provided in the format:
    [flight_no:no_of_passengers, flight_no:no_of_passengers, etc.].'''
    flight_no=[]
    for i in ticket_list:
        
        t=i[:5]
        flight_no.append(t)
    temp=[]
    for i in range(len(flight_no)):
        c=1
        for j in range(i+1,len(flight_no)):
            if flight_no[i]==flight_no[j]:
                c+=1
        if flight_no[i] not in temp:        
            temp.append(flight_no[i])
            temp.append(c)
    result=[]
    for i in range(0,len(temp),2):
        result.append(temp[i]+":"+str(temp[i+1]))
    return(result)    
    

def sort_passenger_list():
   
    temp=[]
    temp=(find_passengers_per_flight())
    srt=[]
    temp2=[]
    for i in temp:
        srt.append(int(i[-1:]))
        temp2.append(int(i[-1:]))
    
    
    res=[]
    addrs=[]
    while(srt):
        maxx=srt[0]
        for i in range(len(srt)):
            if srt[i]>=maxx:
                maxx=srt[i]
                
        tem=temp2.index(maxx)
        srt.remove(maxx)        
        res.append(maxx)

        addrs.append(tem)
    result=[]
    for i in addrs:
        result.append(temp[i])
    return(result)    
    #Remove pass and write your logic here

#Provide different values for airline_name and destination and test your program.
print(find_passengers_flight("AI"))
print(find_passengers_destination("LON"))
print(sort_passenger_list())

