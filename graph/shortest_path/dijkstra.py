"""ダイクストラと経路復元のアルゴリズム"""

from util import initialize_adjlists
from heapq import heappop, heappush

INF = 10 ** 10


def dijakstra(adjacency_lists: dict, start: int):
    V = len(adjacency_lists)
    distances = [INF] * V
    parents = [-1] * V
    done_searchs = [False] * V

    priority_queues = []
    heappush(priority_queues, (0, start))
    done_searchs[start] = True
    distances[start] = 0

    while (len(priority_queues) != 0):
        _, node = heappop(priority_queues)
        next_nodes = adjacency_lists[node]
        for next_node, w in next_nodes:
            if done_searchs[next_node]:
                continue
            else:
                if distances[next_node] > distances[node] + w:
                    distances[next_node] = distances[node] + w
                    parents[next_node] = node
                    heappush(priority_queues, (distances[next_node], next_node))

    return distances, parents


def main():
    V, E, start = map(int, input().split())
    adjacency_lists = {}  # key: node, value: (node, weight)
    adjacency_lists = initialize_adjlists(adjacency_lists, V)

    for _ in range(E):
        from_, to_, w = map(int, input().split())
        adjacency_lists[from_].append((to_, w))

    distances, parents = dijakstra(adjacency_lists, start)

    for i in range(V):
        if distances[i] >= INF:
            print("INF")
        else:
            print(distances[i])


if __name__ == '__main__':
    main()
