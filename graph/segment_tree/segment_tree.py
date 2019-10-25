import sys
sys.setrecursionlimit(10000000)

INF = 2 ** 31 - 1


class SegmentTree():
    def __init__(self, N):
        self.N = 1  # the number of leaves
        while self.N < N:
            self.N = 2 * self.N
        self.nodes = [INF] * (2 * self.N - 1)  # 0 origin


    def find(self, from_, to_, k, left, right):
        """
        return the minimum value between the index of from_ and to_
        k: which node to look at
        """
        if from_ >= left and to_ <= right:
            # include
            return self.nodes[k]

        elif from_ >= left or to_ <= left:
            # partially include
            mid = (left + right) // 2
            return min(self.find(from_, to_, k * 2, left, mid), self.find(from_, to_, k * 2 + 1, mid+1, right))
        else:
            # exclude
            return INF


    def update(self, i, x):
        """
        update the element i into x
        """
        i += self.N - 1
        self.nodes[i] = x
        while (True):
            i = (i - 1) // 2
            self.nodes[i] = min(self.nodes[i * 2 + 2], self.nodes[i * 2 + 1])
            if i == 0:
                break


def main():
    n, q = map(int, input().split())
    segment_tree = SegmentTree(n)
    for _ in range(q):
        com, x, y = map(int, input().split())
        if com == 0:
            segment_tree.update(x, y)
        else:
            if x > y:
                x, y = y, x
            min_ = segment_tree.find(x, y, 1, 1, n)
            print(min_)


if __name__ == '__main__':
    main()
