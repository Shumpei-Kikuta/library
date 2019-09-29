"""約数列挙のプログラム"""

import sys
sys.setrecursionlimit(10000000)


def divisor(N):
    """dが約数とするとN/dも約数。よってdは2~int(N**0.5)まで"""
    divisors = set()
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            divisors.add(i)
            divisors.add(N//i)
            N //= i
    divisors.add(int(N))
    return divisors


def main():
    N = int(input())
    print(divisor(N))


if __name__ == '__main__':
    main()
