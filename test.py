def sum(tree, x):
    s = 0
    while x > 0:
        s += tree[x]
        x -= x & -x
    return s

def add(tree, x, v):
    while x < len(tree):
        tree[x] += v
        x += x & -x

def solve():
    n, q = map(int, input().split())

    arr = []
    for i in range(q):
        arr.append(list(map(int, input().split())))
    
    tree = [0 for i in range(n+5)]
    for i in range(q):
        add(tree, arr[i][0], 1)
        add(tree, arr[i][1]+1, -1)
    
    print(sum(tree, n))

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        solve()