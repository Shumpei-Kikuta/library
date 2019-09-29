"""素因数分解のプログラム O(N**0.5)"""

import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)


def prime_factor(N):
    """dictを返す"""
    factors = {}
    for i in range(2, int(N**0.5)+1):
        while(N % i == 0):
            if factors.get(i) is None:
                factors[i] = 1
            else:
                factors[i] += 1
            N //= i
    if N != 1:
        factors[N] = 1
    return factors

def main():
    N = int(input())
    print(prime_factor(N))


if __name__ == '__main__':
    main()