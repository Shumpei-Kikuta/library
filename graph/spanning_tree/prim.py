"""ダイクストラと経路復元のアルゴリズム"""

from heapq import heappop, heappush

INF = 10 ** 10


def initialize_adjlists(lists, V):
    for i in range(V):
        lists[i] = []
    return lists


def prim(adjacency_lists: dict) -> int:
    V = len(adjacency_lists)
    done_searchs = [False] * V

    priority_queues = []
    heappush(priority_queues, (0, 0))  # 0から探索開始

    num = 0
    while (len(priority_queues) != 0):
        weight, node = heappop(priority_queues)
        if done_searchs[node]:
            continue
        done_searchs[node] = True
        num += weight
        next_nodes = adjacency_lists[node]
        for next_node, w in next_nodes:
            if done_searchs[next_node]:
                continue
            else:
                heappush(priority_queues, (w, next_node))


    return num


def main():
    V = int(input())
    adjacency_lists = {}  # key: node, value: (node, weight)
    adjacency_lists = initialize_adjlists(adjacency_lists, V)

    for i in range(V):
        lists = [int(c) for c in input().split()]
        for j, w in enumerate(lists):
            if w == -1:
                continue
            adjacency_lists[i].append((j, w))

    print(prim(adjacency_lists))


if __name__ == '__main__':
    main()
