#PF-Assgn-39
     


menu=('Veg Roll','Noodles','Fried Rice','Soup')
quantity_available=[2,200,3,0]


def place_order(*item_tuple):
    quantity_required_list=[]
    items_list=[]
    for i in range(len(item_tuple)//2):
        items_list.append(item_tuple[2*i])
        quantity_required_list.append(item_tuple[2*(i)+1])
    for i in range(len(items_list)):
        if items_list[i] not in menu:
            print(items_list[i]+" is not available")
        else:    
            for j in range(len(menu)):
                if menu[j]==items_list[i]:
                    temp=j
                    
                    available=check_quantity_available(quantity_available[j],quantity_required_list[i])
                    if (available):
                        print (items_list[i]+" is available")
                        quantity_available[j]-=quantity_required_list[i]
                    else:
                        print(items_list[i]+" stock is over")

    
def check_quantity_available(index,quantity_requested):
    if (index>=quantity_requested):
        return True
    else:
        return False


place_order("Fried Rice",2,
"Soup",1)
