"""ユークリッドの互除法"""


def swap(a, b):
    return b, a


def gcd(a, b):
    X = max(a, b)
    Y = min(a, b)
    step = 0
    while(Y != 0):
        X %= Y
        X, Y = swap(X, Y)
        step += 1
    return X, step


def main():
    while(True):
        X, Y = map(int, input().split())
        if X == 0 and Y == 0:
            break
        else:
            maximum_divisor, step = gcd(X, Y)
            print(maximum_divisor, step)


if __name__ == '__main__':
    main()
