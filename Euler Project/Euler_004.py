#
# Solution to HackerRank Project Euler - Problem 4
# Copyright (c) Saribalidis John. All rights reserved.
# 
# Project Euler #4: Largest palindrome product
# https://www.hackerrank.com/contests/projecteuler/challenges/euler004
#
# https://github.com/jsari/HackerRank
# 

def get_palindromes(n):
    """
    Returns all 6-digits palindromes until n in reversed order
    """
    
    for number in range(int(str(n)[:3]), 100, -1):
        res = int(str(number) + str(number)[::-1])
        if res < n:
            yield res


def is_product(n):

    """
    Checks if 6-digit number n is a product of two 3-digit numbers
    """

    i = 101
    while i <= 999:
        if n % i == 0 and 100 <= n / i <= 999:
            return True
        i = i + 1

    return False


if __name__ == '__main__':

    for _ in range(int(input())):
        for num in palindromes(int(input())):
            if is_product(num):
                print(num)
                break