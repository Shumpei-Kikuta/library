import sys
sys.setrecursionlimit(10000000)

INF = 10 ** 8


class SegmentTree():
    def __init__(self, N):
        self.N = N
        self.nodes = [INF] * (2 * N + 1)


    def find(self, from_, to_):
        """
        from_からto_までの最小値を返す
        """
        pass


    def update(self, i, x):
        """
        i番目の要素をxに変更する
        """
        pass    


def main():
    n, q = map(int, input().split())
    segment_tree = SegmentTree(n)
    for _ in range(q):
        com, x, y = map(int, input().split())
        if com == 0:
            segment_tree.update(x, y)
        else:
            segment_tree.find(x, y)



if __name__ == '__main__':
    main()
