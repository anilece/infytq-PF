
import sys

sys.setrecursionlimit(10000)
def fibonacci(num):
    memo.update({0: 0})
    memo.update({1: 1})
    if num in memo.keys():
        return(memo[num])
    else:
        temp=fibonacci(num-1)+fibonacci(num-2)
        memo.update({num:temp})
        return(memo[num])

memo={}

print("Fibonacci number:",fibonacci(49))
