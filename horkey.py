import collections
import sys
sys.stdin = open("input.txt","r")

def bfs(arr, start_node):
    visit = []
    queue = collections.deque()

    queue.append(start_node)

    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.append(node)
            for ar in arr:
                if ar[0] == node:
                    queue.append(ar[1])
    return visit

def dfs(arr, start_node):
    visit = []
    stack = []
    stack.append(start_node)


    while stack:
        print(stack)
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            for ar in arr:
                if ar[0] == node:
                    stack.append(ar[1])
    return visit
    


N, M, V = list(map(int,input().split()))
arr = [list(map(int,input().split())) for i in range(M)]
print(*dfs(arr,1))
print(*bfs(arr,1))