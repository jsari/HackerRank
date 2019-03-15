#
# Solution to HackerRank Project Euler - Problem 1
# Copyright (c) Saribalidis John. All rights reserved.
#
# Project Euler #1: Multiples of 3 and 5
# https://www.hackerrank.com/contests/projecteuler/challenges/euler001
#
# https://github.com/jsari/HackerRank


def compute(n):

    # compute multiplies of 3, 5 and 15
    total_3 = int(3 * (n // 3) * (1 + n // 3) // 2)
    total_5 = int(5 * (n // 5) * (1 + n // 5) // 2)
    total_15 = int(15 * (n // 15) * (1 + n // 15) // 2)

    total = total_3 + total_5 - total_15

    return total


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input()) - 1
        print(compute(n))
