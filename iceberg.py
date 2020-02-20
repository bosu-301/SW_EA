N, M = list(map(int,input().split()))
arr = [list(map(int,input().split())) for i in range(N)]

tmp_arr = [[0]*M for i in range(N)]


dr = [0,0,1,-1]
dc = [1,-1,0,0]

while True:
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
