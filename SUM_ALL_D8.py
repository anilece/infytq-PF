

def sum_all(function, data):
     #Remove pass and write the logic here
    res_sum=0
    for w in data:
        if (function(w)):
            res_sum+=w
    return res_sum
list_of_nos=[100,200,300,500,1040]

greater = lambda num :num>10


divide = lambda num:((num%10==0) and num <=100)


range_of_values = lambda num:(num>25 and num<50)

print(sum_all(greater,list_of_nos))
print(sum_all(divide,list_of_nos))
print(sum_all(range_of_values,list_of_nos))
