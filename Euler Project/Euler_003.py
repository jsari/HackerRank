#
# Solution to HackerRank Project Euler - Problem 3
# Copyright (c) Saribalidis John. All rights reserved.
# 
# Project Euler #3: Largest prime factor
# https://www.hackerrank.com/contests/projecteuler/challenges/euler003
#
# https://github.com/jsari/HackerRank
# 

def get_max_prime_factor(n):
    '''
    Compute the largest prime factor of  number n
    '''
    max_factor = 1
    
    while n % 2 == 0:
        max_factor = 2
        n = n // 2

    i = 3
    while i * i <= n:
        while n % i == 0:
            n = n // i
            max_factor = i
        i = i + 2

    if n > 2:
        return n
    else:
        return max_factor


if __name__ == '__main__':

    for _ in range(int(input())):
        print(max_prime_factor(int(input())))