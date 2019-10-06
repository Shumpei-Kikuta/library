"""クラスカル法"""


class Node:
    def __init__(self, idx):
        self.idx = idx
        self.parent = None


def unite(x: Node, y: Node, nodes):
    """xを含む集合とyを含む集合を併合"""
    x_root, x_depth = root(x, 0)
    y_root, y_depth = root(y, 0)

    # xの根を併合後の根とする
    if y_root != x_root:
        if x_depth >= y_depth:
            y_root.parent = x_root
            nodes[y_root.idx] = y_root
        else:
            x_root.parent = y_root
            nodes[x_root.idx] = x_root
    return nodes


def same(x: Node, y: Node):
    """xとyが同じ集合に所属するか？すれば1, しなければ0を返す"""
    x_root, _ = root(x, 0)
    y_root, _ = root(y, 0)
    if x_root.idx == y_root.idx:
        return 1
    else:
        return 0


def root(x: Node, cnt: int):
    """Node xの所属する木の根を探索"""
    if x.parent is None:
        return x, cnt
    else:
        return root(x.parent, cnt + 1)


def initialize_adjlists(lists, V):
    for i in range(V):
        lists[i] = []
    return lists


def adjacency_lists2kuraskal_list(adjacency_lists: dict) -> dict:
    """
    OUTPUT: {(from_, to_): weight}
    """
    dicts = {}
    for from_ in adjacency_lists:
        for to_, weight in adjacency_lists[from_]:
            dicts[(from_, to_)] = weight
    return dicts


def kuraskal(adjacency_lists: dict):
    V = len(adjacency_lists)
    kuraskal_lists = adjacency_lists2kuraskal_list(adjacency_lists)
    kuraskal_lists = sorted(kuraskal_lists.items(), key=lambda x: x[1])

    nodes = []
    for i in range(V):
        node = Node(i)
        nodes.append(node)

    num = 0
    for (from_, to_), weight in kuraskal_lists:
        if same(nodes[from_], nodes[to_]):
            continue
        else:
            nodes = unite(nodes[from_], nodes[to_], nodes)
            num += weight
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

    print(kuraskal(adjacency_lists))


if __name__ == '__main__':
    main()
