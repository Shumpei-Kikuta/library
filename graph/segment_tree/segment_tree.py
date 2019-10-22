import sys
sys.setrecursionlimit(10000000)


INF = 10 ** 8

class SegmentTree():
    def __init__(self, N, A):
        self.N = N
        self.nodes = [INF] * (2 * N)
        self.__init(A)


def query():


def update():


def __init(self, A):
    # initialize the segment tree
    # initialize the lists
    for i in range(N, 2*N):
        self.nodes[i] = A[i - N]
    
    #  initialize the minimum
    
    



def main():
    N = int(input())
    A = [int(c) for c in input().split()]
    segment_tree = SegmentTree(N, A)



if __name__ == '__main__':
    main()
