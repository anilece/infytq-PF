
package main

import ("fmt")
func Find_square( Given_num int) int{
        var Square_num int=Given_num*Given_num
        return (Square_num) 
    }
func main() {
    /
    
    var Given_num int =3
    var Result int =Find_square(Given_num)
    fmt.Println(Result)    
}
