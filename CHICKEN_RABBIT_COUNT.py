def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    if (legs%2==1 or heads>legs):
        print(error_msg)
    else:    
        rabbit_count=(legs//2)-heads
        chicken_count=heads-rabbit_count
        print(chicken_count,rabbit_count)
    

solve(150,400)
