"""N以下の素数を列挙、N以下の素数の数 O(NloglogN) (ほぼO(N))"""

def calc_eratosthenes(N):
    is_primes = [True] * (N + 1)
    is_primes[0], is_primes[1] = False, False
    primes = []
    for i in range(2, N + 1):
        if is_primes[i]:
            primes.append(i)
            k = 2
            while(k * i <= N):
                is_primes[k * i] = False
                k += 1
        else:
            continue
    return primes, len(primes)


def main():
    N = int(input())
    lists, num = calc_eratosthenes(N)
    print(num)


if __name__ == '__main__':
    main()
