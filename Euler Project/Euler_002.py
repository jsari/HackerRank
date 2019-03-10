#
# Solution to HackerRank Project Euler - Problem 2
# Copyright (c) Saribalidis John. All rights reserved.
# 
# Project Euler #2: Even Fibonacci numbers
# https://www.hackerrank.com/contests/projecteuler/challenges/euler002
#
# https://github.com/jsari/HackerRank
# 

def fib(n):
    '''
    Compute the sum of the even-valued Fibonacci terms 
    whose values do not exceed number n
    '''
    
    total = 2
    a, b = 1, 2
    while a+b <= n:        
        f = a+b
        if f%2 == 0:
            total = total+f
        a, b = b, f
    
    return total
    
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        print( fib(n))