#PF-Assgn-29
def calculate(distance,no_of_passengers):
    Price_per_litre = 70
    Mileage_of_bus = 10
    Price_per_ticket = 80
    Total_cost_bus=(distance/Mileage_of_bus)*Price_per_litre
    Total_cost_Passengers=no_of_passengers*Price_per_ticket
    if(Total_cost_Passengers>Total_cost_bus):
        return(Total_cost_Passengers-Total_cost_bus)
    else:
        return(-1)
    


distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))
