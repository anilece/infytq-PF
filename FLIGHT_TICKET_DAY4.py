#PF-Exer-22

def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[""]*no_of_passengers
    
    for i in range(no_of_passengers):
        num=100+i+1
        ticket_number_list[i]=airline+":"+source[0:3]+":"+destination[0:3]+':'+str(num)
    
    if (no_of_passengers>5):
        ticket_number_list=ticket_number_list[-5:]
        
    return ticket_number_list


print(generate_ticket("AI","Bangalore","London",7))
