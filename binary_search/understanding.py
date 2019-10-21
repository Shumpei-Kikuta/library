"""
定義
lower_bound(A, k): はじめてk以上となるindex
upper_bound(A, k); はじめてkより大きくなるindex
"""

import bisect


def main():
    """
    配列の中にkが1つ存在するケース
    """
    A = [1, 2, 3, 4, 5]
    k = 3
    print("lower_bound: ", bisect.bisect_left(A, k))
    print("upper_bound: ", bisect.bisect_right(A, k))

    """
    配列の中にkが存在しないケース
    -> lower_boundとupper_boundが同じになる
    """
    A = [1, 2, 4, 5]
    k = 3
    print("lower_bound: ", bisect.bisect_left(A, k))
    print("upper_bound: ", bisect.bisect_right(A, k))

    """
    配列の中にkが1つ存在するケース
    """
    A = [1, 2, 3, 3, 3, 4, 5]
    k = 3
    print("lower_bound: ", bisect.bisect_left(A, k))
    print("upper_bound: ", bisect.bisect_right(A, k))


if __name__ == '__main__':
    main()
