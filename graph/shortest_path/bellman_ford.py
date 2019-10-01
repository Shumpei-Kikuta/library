"""負の辺がある場合に利用。負の閉路の検出も可能 O(V * E)"""

INF = 10**10

def initialize_adjlists(lists, V):
    for i in range(V):
        lists[i] = []
    return lists

def shortest_path(shortest_paths, adjacency_lists):
    update = True
    cnt = 0
    V = len(adjacency_lists)
    while(update):
        cnt += 1

        if cnt > V:
            # N回を超えるループ→負の経路がある
            return [], "NEGATIVE CYCLE"

        update = False
        for from_ in adjacency_lists:
            for to_, w in adjacency_lists[from_]:
                if shortest_paths[from_] != INF and shortest_paths[to_] > shortest_paths[from_] + w:
                    shortest_paths[to_] = shortest_paths[from_] + w
                    update = True
    
    return shortest_paths, None


def main():
    V, E, r = map(int, input().split())
    adjacency_lists = {}
    adjacency_lists = initialize_adjlists(adjacency_lists, V)
    for _ in range(E):
        from_, to_, w = map(int, input().split())
        adjacency_lists[from_].append((to_, w))
    shortest_paths = [INF] * V
    shortest_paths[r] = 0
    shortest_paths, error = shortest_path(shortest_paths, adjacency_lists)

    if error is not None:
        print(error)
    else:
        for i in shortest_paths:
            if i == INF:
                print("INF")
            else:    
                print(i)


if __name__ == '__main__':
    main()