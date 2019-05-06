#PF-Assgn-16
def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    f=rupees_to_make//5
    while (f>no_of_five):
        f-=1
    o=rupees_to_make-(f*5)
    if(o<=no_of_one):
        one_needed=o
        five_needed=f
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
    else:
        print(-1)
    
   

#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(28,8,5)
