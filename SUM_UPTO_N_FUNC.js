Function Find_sum_uptoN(Given_val){
    Sum=0
    for (int i=1;i<=Given_val;i++){
        Sum=Sum+i
    }
    return(Sum)
}
Given_val=5
Result=Find_sum_uptoN(Given_val)
console.log(Result)
