from util import initialize_adjlists

INF = 10 ** 12


def check(dp):
    V = len(dp)
    for i in range(V):
        if dp[i][i] < 0:
            return True
    return False


def initialize_triple_lists(V):
    dp = []
    for _ in range(V):
        lists = []
        for j in range(V):
            lists.append(INF)
        dp.append(lists)
    return dp


def warshall_floyd(adjacency_lists: list):
    V = len(adjacency_lists)
    dp = []
    dp = initialize_triple_lists(V)

    for i in range(V):
        dp[i][i] = 0

    for from_ in adjacency_lists.keys():
        for to_, w in adjacency_lists[from_]:
            dp[from_][to_] = w

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dp[i][j]= min(dp[i][k] + dp[k][j], dp[i][j])
    return dp


def main():
    V, E = map(int, input().split())
    adjacency_lists = {}
    adjacency_lists = initialize_adjlists(adjacency_lists, V)
    for _ in range(E):
        from_, to_, w = map(int, input().split())
        adjacency_lists[from_].append((to_, w))
    
    dp = warshall_floyd(adjacency_lists)

    if check(dp):
        print("NEGATIVE CYCLE")
    else:
        for i in range(V):
            for j in range(V):
                if dp[i][j] >= INF/10:
                    print("INF", end="")
                else:
                    print(dp[i][j], end="")
                if j != V - 1:
                    print(end=" ")
            print()


if __name__ == '__main__':
    main()