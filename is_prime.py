def is_prime(N):
    """Nを2~int(N**0.5)までで割る"""
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            return False
    return True


def main():
    N = int(input())
    if is_prime(N):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
