//PF-Exer-16

num1=5
num2=10


product=num1*num2
while((product>=num1) or (product>=num2))
{
    minimum=0
    if (num1<num2){
        minimum=num1
    }
    else{
        minimum=num2
    }
    
    product-=minimum
    if((product%num1==0) and (product%num2==0))
    {
        product=product
    }
}
console.log(product)
