import turtle          
wn = turtle.Screen()   
wn.setup(500,500)      

alex = turtle.Turtle()  
alex.shape("turtle")   
alex.color("green")    
alex.right(0)        
alex.circle(30)     
alex.circle(50)
for counter in range(1,3):
    alex.circle(20*counter)
alex.color("blue")    
alex.right(120)       
alex.circle(30)      
alex.circle(50)
for counter in range(1,3):
    alex.circle(20*counter)
alex.color("red")   
alex.right(120)         
alex.circle(30)       
alex.circle(50)
for counter in range(1,3):
    alex.circle(20*counter)
