N = int(input())

arr = [list(map(int, input().split()) for i in range(N)]

from itertools import combinations


coms = combinations(range(N),N//2)
for com in coms:
    diff = 999
    
    for i in range(N):
        for j in range(N):
            if i in com and j in com:
                arr[i][j] +=
